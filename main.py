# -*- coding: utf-8 -*-
from odoos.fetchmsg import Aliexpress
from odoos import pushmsg


if __name__ == '__main__':
    threads = []
    aliexpress = Aliexpress()
    sync_stock = aliexpress.stock_order_msg
    threads.append(aliexpress.rolling_thread([aliexpress.shops[0]], 60*60))
    threads.append(aliexpress.rolling_msg_thread())
    threads.append(pushmsg.PuschAliexpress(sync_stock).rolling_thread(10))

    for t in threads:
        t.start()
