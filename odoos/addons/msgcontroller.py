# -*- coding: utf-8 -*-
import Queue
from odoos.tools.MyConfig import config
import logging
import threading
LOCK = threading.Lock()
_logging = logging.getLogger(__name__)


class Controller(object):

    def __init__(self, msgstock):
        self.msgstock = msgstock # 栈
        self.MAXT = config.get('max_thread') or 10 #最大访问odoo线程数

    def create_thread(self):
        pass

    @staticmethod
    def call_odoos(params, db_name=None, user_name=None, user_password=None, method_name=None):
        try:
            db_name = db_name or config.get('db_name')
            user_name = user_name or config.get('user_name')
            user_password = user_password or config.get('user_password')
            method_name = method_name or config.get('method_name')
        except Exception, e:
            _logging.error(e)
