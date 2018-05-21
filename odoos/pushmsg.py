# -*- coding: utf-8 -*-
from odoos.tools.MyConfig import config
import threading
import time
from odoos.tools import api
from odoos.tools.OdooCall import OdooCall
from odoos.tools.mylogging import Logging
_logging = Logging(__name__)


class PuschAliexpress(object):
    def __init__(self, stock):
        self.stock = stock
        self._lock = threading.Lock()
        self._rolling = True
        self.oc = OdooCall(config.get("user_id"), config.get("password"), config.get("dbname"))

    def rolling_thread(self, delay_time=10*60):
        """
        创建循环拉取信息线程
        :param delay_time: 多久循环一次
        :return:
        """

        def target_roll(cls, dt):
            while cls.get_rolling():
                cls.call_odoom()
                time.sleep(dt)
        return threading.Thread(target=target_roll, args=[self, delay_time])

    @api.synchronized()
    def stop_fetchmsg(self):
        self._rolling = False

    @api.synchronized()
    def get_rolling(self):
        return self._rolling

    def call_odoom(self):
        """
        请求odoo方法，创建销售单
        :return:
        """
        params = self.stock.get()
        try:
            res = self.oc.create_aliexpress_order(params)
            if res.get('result', False):
                _logging.info('create aliexpress order success with aliexpress_name = {}'.format(res['result']))
            else:
                _logging.info('allready excit!')
        except Exception, e:
            _logging.error(e)
            self.stock.put(params)
            _logging.info("reset params into unhandle stock")
