# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import time
from dateutil.relativedelta import relativedelta
from flask import json
import top
from odoos.tools.dingUtls import dp
from odoos.tools.MyConfig import config, HEADERS
from odoos.addons.mystock import MyStock
import threading
from odoos.tools import api
from odoos.tools.OdooCall import OdooCall
from odoos.tools.mylogging import Logging

_logging = Logging(__name__)

order_status = [
    "PLACE_ORDER_SUCCESS",  # 0 等待买家付款;
    "IN_CANCEL",  # 1 买家申请取消;
    "WAIT_SELLER_SEND_GOODS",  # 2 等待您发货;
    "SELLER_PART_SEND_GOODS",  # 3 部分发货;
    "WAIT_BUYER_ACCEPT_GOODS",  # 4 等待买家收货;
    "FUND_PROCESSING",  # 5 买家确认收货后，等待退放款处理的状态;
    "FINISH",  # 6 已结束的订单;
    "IN_ISSUE",  # 7 含纠纷的订单;
    "IN_FROZEN",  # 8 冻结中的订单;
    "WAIT_SELLER_EXAMINE_MONEY",  # 9 等待您确认金额;
    "RISK_CONTROL",  # 10 订单处于风控24小时中，从买家在线支付完成后开始，持续24小时。
]


class Aliexpress(object):
    def __init__(self, split_type=','):
        self.shops = config.get('shops').split(split_type)
        self.stock_order_ids = MyStock(int(config.get('maxsize')) if config.get('maxsize') else 10000)
        self.stock_order_msg = MyStock(int(config.get('maxsize')) if config.get('maxsize') else 10000)
        self._lock = threading.Lock()
        self._rolling = True
        self.oc = OdooCall(config.get("user_id"), config.get("password"), config.get("dbname"))

    def rolling_thread(self, shops=None, delay_time=10*60):
        """
        创建循环拉取订单order_id线程
        :param shops: list
        :param delay_time:
        :return:
        """

        def target_roll(cls, ss, dt):
            while cls.get_rolling():
                cls.get_sale_lists(ss)
                time.sleep(dt)
        return threading.Thread(target=target_roll, args=[self, shops, delay_time])

    def rolling_msg_thread(self, delay_time=10):
        """
        创建循环拉取订单详情线程
        :param shops: list
        :param delay_time:
        :return:
        """

        def target_roll_msg(cls, dt):
            while cls.get_rolling():
                cls.get_sale_msg()
                time.sleep(dt)
        return threading.Thread(target=target_roll_msg, args=[self, delay_time])

    @api.synchronized()
    def stop_fetchmsg(self):
        self._rolling = False

    @api.synchronized()
    def get_rolling(self):
        return self._rolling

    def get_sale_lists(self, shops=None):
        if not shops:
            shops = self.shops
        for shop in shops:
            # 订单列表简化查询
            create_date_end, create_date_start = self._get_start_end_time(shop)
            page, page_size, total_item = 1, 50, 51
            order_lists = []
            while page * page_size < total_item:
                req = top.api.AliexpressTradeRedefiningFindorderlistsimplequeryRequest("gw.api.taobao.com", 80)
                req.set_app_info(top.appinfo(config.get("appkey", shop), config.get("secret", shop)))
                req.param1 = {"create_date_end": create_date_end,
                              "create_date_start": create_date_start,
                              "page": page,
                              "page_size": page_size,
                              "order_status": order_status[0]
                              }
                try:
                    resp = req.getResponse(config.get("session", shop))
                    total_item = int(resp.get('aliexpress_trade_redefining_findorderlistsimplequery_response', {}).get('result', {}).get('total_item', total_item))
                    _logging.info("total_item=" + str(total_item) + "  page=" + str(page))
                    li = self.load_findorderlistsimplequery_response(resp, shop)
                    order_lists += li
                except Exception, e:
                    _logging.error(e)
                    if hasattr(e, 'errorcode') and e.errorcode == 15:
                        self._send_to_ding("请跳转到：{}进行人工授权".format(self.get_access_token(shop)))
                    break
                page += 1
            if order_lists:
                order_lists = self.oc.check_repeat(order_lists)
                lis = order_lists.get('result', [])
                self.stock_order_ids.put_list(lis)
                _logging.info("put_list into stock_order_ids" + str(lis))
            # TODO 将create_date_end，create_date_start，page，page_size 回写回配置文件
            self._write_next_start_end_time(create_date_start, create_date_end, shop)

    def get_sale_msg(self):
        package_size = config.get('package_size') or 50
        if self.stock_order_ids.ssize() > 0:
            _logging.info("get order masg, package_size = " + str(package_size))
            order_ids = self.stock_order_ids.get_list(package_size)
            _logging.info("order_ids = " + str(order_ids))
            msg_lists = []
            for i in order_ids:
                # 订单详情查询
                req = top.api.AliexpressTradeRedefiningFindorderbyidRequest("gw.api.taobao.com", 80)
                req.set_app_info(top.appinfo(config.get("appkey", i[1]), config.get("secret", i[1])))
                req.param1 = {"order_id": i[0]}
                try:
                    resp = req.getResponse(config.get("session", i[1]))
                    msg = self.load_findorderbyid_response(resp, i[1])
                    msg_lists.append(msg)
                    _logging.info("append a msg " + str(i[0]))
                except Exception, e:
                    _logging.error(e)
                    if hasattr(e, 'errorcode') and e.errorcode == 15:
                        self._send_to_ding("请跳转到：{}进行人工授权".format(self.get_access_token(i[1])))
                    else:
                        self._send_to_ding("拉取订单详情失败：{}".format(i[0]))
            _logging.info('put msg list' + str(len(msg_lists)))
            self.stock_order_msg.put(msg_lists)

    def load_findorderlistsimplequery_response(self, resp, shop):
        """
        解析AliexpressTradeRedefiningFindorderlistqueryRequest返回的内容
        :param resp: 返回内容
        :return: [{},{},]
        """
        order_list = []
        if 'aliexpress_trade_redefining_findorderlistsimplequery_response' in resp:
            for i in resp['aliexpress_trade_redefining_findorderlistsimplequery_response']['result']['order_list']['simple_order_item_vo']:
                order_list.append([i['order_id'], shop])
        return order_list

    def load_findorderbyid_response(self, resp, shop):
        """
        解析订单详情信息
        :param resp: 接口返回信息
        :param shop: 配置文件店铺名称
        :return:
        """
        if 'aliexpress_trade_redefining_findorderbyid_response' in resp:
            res = resp['aliexpress_trade_redefining_findorderbyid_response']['result']
            res.update({'shop_code': config.get('shop_code', shop)})
            return res
        return []


    def _get_start_end_time(self, shop=None):
        """
        获取该店铺拉取时间
        delay_time 是拉取多长分钟前的订单，只在第一次运行中有用
        last_run_time 是上次运行时间，将在上次结束和开始时间上加上该值生成本次运行开始结束时间
        :param shop:
        :return: (create_date_end, create_date_start)
        """
        last_run_time = config.get("last_run_time", shop) or time.time()
        last_run_time = int((int(float(last_run_time)) - time.time())/60)
        delay_time = config.get("delay_time", shop)
        create_date_end_default = config.get("create_date_end", shop) if config.get("create_date_end", shop) else \
            datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        create_date_start_default = config.get("create_date_start", shop) if config.get("create_date_start", shop) else \
            (datetime.strptime(create_date_end_default, '%m/%d/%Y %H:%M:%S') -
             relativedelta(minutes=delay_time or 2*24*60)).strftime('%m/%d/%Y %H:%M:%S')

        create_date_start = (datetime.strptime(create_date_start_default, '%m/%d/%Y %H:%M:%S') +
                             relativedelta(minutes=last_run_time)).strftime('%m/%d/%Y %H:%M:%S')
        create_date_end = (datetime.strptime(create_date_end_default, '%m/%d/%Y %H:%M:%S') +
                             relativedelta(minutes=last_run_time)).strftime('%m/%d/%Y %H:%M:%S')
        return create_date_end, create_date_start

    def _write_next_start_end_time(self, create_date_start, create_date_end, shop=None):
        """
        写入下次执行开始和结束时间
        :param shop:
        :return:
        """
        params = {
            'last_run_time': time.time(),
            'create_date_end': create_date_end,
            'create_date_start': create_date_start,
        }
        config.write(params, shop)



    def update_aliexpress_token(self, shop=None, repeat_times=3):
        """
        更新token 现在token固定时长为1年，此方法不可用
        :param shop:
        :param repeat_times: 重试次数
        :return:
        """
        shops = self.shops
        if shops and shop in shops:
            shops = [shop]
        for shop_id in shops:
            url = 'https://gw.api.alibaba.com/openapi/param2/1/system.oauth2/getToken/{}'.format(
                config.get("appkey", shop_id))
            # url = "https://oauth.taobao.com/token"
            refresh_token_config = config.get("refresh_token", shop_id)
            data = {
                'grant_type': 'refresh_token',
                'client_id': config.get("appkey", shop_id),
                'client_secret': config.get("secret", shop_id),
                'refresh_token': refresh_token_config
            }
            try:
                refresh_response = requests.post(url=url, data=data, headers=HEADERS, timeout=5)
                if hasattr(refresh_response, 'status_code') and refresh_response.status_code > 200:
                    if refresh_response.status_code == 401:
                        while repeat_times > 0:
                            self.update_aliexpress_token(shop_id)
                            repeat_times -= 1
                        _logging.info(
                            u'请跳转到：{}进行人工授权;'.format(self.get_access_token(shop_id)))
                    raise ValueError(refresh_response.text)
                response_json = refresh_response.json()
            except requests.exceptions.Timeout, e:
                _logging.info(u'更新AliExpress Token,调用速卖通接口超时：{e}'.format(e=e))
                pass
            except Exception, e:
                _logging.info(u'更新AliExpress Token,调用速卖通接口产生了一个异常：{e}'.format(e=e))
                pass
            else:
                if 'access_token' in response_json and response_json['access_token']:
                    _logging.info(u'update access_token:{}'.format(response_json['access_token']))
                    shop_id.write({'access_token': response_json['access_token'],
                                   'refresh_token': response_json['refresh_token']})
                else:
                    self._send_to_ding(u'更新AliExpress Token失败')
            pass

    def _send_to_ding(self, msg):
        url = config.get('aliexpress_error_ding')
        text_phone = config.get('text_phone') if config.get('text_phone') else ''
        param = json.dumps(
            {
                "msgtype": "text",
                "text": {
                    "content": text_phone + ' ' + __name__ + str(msg) + "\n"
                },
                "at": {
                    "atMobiles": [text_phone],
                    "isAtAll": False
                }
            }
        )
        dp._do_post(url, param)

    def get_access_token(self, state=None):
        return "https://oauth.aliexpress.com/authorize?response_type=token&client_id={}&state=1212&view=web&sp=ae".format(
            config.get('appkey', state))
