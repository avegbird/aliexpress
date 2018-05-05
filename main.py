# -*- coding: utf-8 -*-
from odoos.fetchmsg import Aliexpress, _logging
from odoos import pushmsg

if __name__ == '__main__':
    _logging.new_logfile()
    threads = []
    aliexpress = Aliexpress()
    sync_stock = aliexpress.stock_order_msg
    threads.append(aliexpress.rolling_thread([aliexpress.shops[0]], 60*60))
    threads.append(aliexpress.rolling_msg_thread())
    threads.append(pushmsg.PuschAliexpress(sync_stock).rolling_thread(60*2))

    for t in threads:
        t.start()
