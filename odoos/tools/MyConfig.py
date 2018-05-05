# -*- coding: utf-8 -*-
import ConfigParser
import os, sys
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
}


class MyConfig(object):
    """
    1，加载配置文件
    2，更新配置文件
    """
    def __init__(self):
        args = sys.argv[1:]
        options = {}

        if not args:
            args = []
        for i in args:
            if i.startswith("-c=") or i.startswith("--config="):
                options.update({'config_path': i[i.find("=") + 1:]})
            if i.startswith("-l=") or i.startswith("--start_level"):
                options.update({'start_state': i[i.find("=") + 1:]})
        self.config_path = None
        if 'config_path' in options:
            if os.path.exists(options['config_path']):
                self.config_path = os.path.abspath(options['config_path'])
        else:
            if os.path.exists('./config/aliexpress.conf'):
                self.config_path = os.path.abspath('./config/aliexpress.conf')
        if not self.config_path:
            raise ValueError("未找到配置文件！")
        if 'start_state' in options:
            self.start_state = options['start_state']
        else:
            raise ValueError("缺少起始配置项！")
        self.cp = ConfigParser.ConfigParser()
        self.cp.read(self.config_path)
        self.options = self.cp.options(self.start_state)

    def get(self, opt, state=None):
        if state is None:
            state = self.start_state
        opts = self.cp.options(state)
        if opt in opts:
            return self.cp._sections[state][opt]
        return ''

    def write(self, dicts, shop=None):
        """
        将信息回写回配置文件
        :param dicts: 需要回写的配置项
        :param shop: shop_options 默认为空，则为start_state
        :return:
        """
        options = str(shop) if shop else self.start_state
        for key, val in dicts.items():
            self.cp.set(options, str(key), str(val))
        with open(self.config_path, "w") as wf:
            self.cp.write(wf)

config = MyConfig()