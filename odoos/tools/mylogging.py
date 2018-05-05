# -*- coding: utf-8 -*-
import logging
import zipfile

from MyConfig import config
import os
from datetime import datetime


class Logging(object):
    def __init__(self, logname, log_file=None, logging_level=None):
        logger = logging.getLogger(logname)
        if not logging_level:
            logging_level = logging.INFO
        if not log_file:
            log_file = config.get("log_file") if config.get("log_file") else "./log.txt"
        logger.setLevel(level=logging_level)
        self.log_file = log_file
        self.handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        logger.addHandler(self.handler)
        self.log = logger

    def info(self, msg):
        self.log.info(msg)

    def error(self, msg):
        self.log.error(msg)

    def new_logfile(self, logname=None, logging_level=logging.INFO):
        try:
            logging._acquireLock()
            if self.log and self.handler:
                self.log.removeHandler(self.handler)
            else:
                self.log = logging.getLogger(logname)
                self.log.setLevel(level=logging_level)
            if os.path.exists(self.log_file):
                back_file_path = os.path.abspath(config.get('back_file_path')) if os.path.abspath(config.get('back_file_path')) else os.path.dirname(os.path.abspath(self.log_file))
                if not os.path.exists(back_file_path):
                    os.makedirs(back_file_path)
                back_file_name = os.path.join(back_file_path, datetime.now().strftime('%Y%m%d%H%M%S') + 'log_bck.txt')
                zf = zipfile.ZipFile(back_file_name, 'w')
                zf.write(os.path.abspath(self.log_file))
                os.remove(os.path.abspath(self.log_file))
                zf.close()
            else:
                raise ValueError('目录不存在')
            # 重新定向log输出文件
            self.handler = logging.FileHandler(self.log_file)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            self.handler.setFormatter(formatter)
            self.log.addHandler(self.handler)
        finally:
            logging._releaseLock()