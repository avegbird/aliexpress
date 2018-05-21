# -*- coding: utf-8 -*-
import urllib2
from flask import json
from odoos.tools.MyConfig import config
from odoos.tools.mylogging import Logging

_logging = Logging(__name__)


class OdooCall(object):
    """
    封装访问odoo rpc方法
    """
    def __init__(self, user_id, password, dbname):
        self.dbname = dbname
        self.user_id = user_id
        self.password = password

    def updateAppInfo(self, user_id, password, dbname):
        self.dbname = dbname
        self.user_id = user_id
        self.password = password

    def _call_odoo(self, model, method, params={}):
        """
        调用odoo rpc方法
        :param model: 方法model
        :param method: 方法名称
        :param params: 参数
        :return: json respone
        """
        url = config.get('host')
        args = [self.dbname, self.user_id, self.password, model, method]
        if params:
            args.append(params)
        else:
            _logging.info('odoo call params is null')
        data = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                 "service": "object",
                 "method": "execute",
                 "args": args},
            "id": 200}
        header = {'Content-Type': 'application/json'}
        data = json.dumps(data)
        req = urllib2.Request(url=url, data=data, headers=header)
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()
        data = json.loads(response)
        # _logging.info(json.dumps(data))
        if data.get('result',{}).get('success', False):
            _logging.info('odoo call success')
            return data['result']
        else:
            _logging.info('odoo call error')
            raise ValueError(data['error'] if 'error' in data else "unknow error code")

    def create_aliexpress_order(self, params):
        _logging.info('create_aliexpress_order')
        return self._call_odoo('aliexpress.sale.order', 'create_aliexpress_order', params)
        # return self._call_odoo('logistics.record', "get_logistics_company", params)

    def check_repeat(self, order_ids):
        _logging.info('check_repeat')
        return self._call_odoo('aliexpress.sale.order', 'check_repeat', order_ids)
