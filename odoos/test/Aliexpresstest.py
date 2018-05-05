# -*- coding: utf-8 -*-

from odoos.fetchmsg import Aliexpress
import time

aliexpress = Aliexpress()
sync_stock = aliexpress.stock_order_msg
t1 = aliexpress.rolling_thread([aliexpress.shops[0]], 5)
t1.start()
time.sleep(20)
aliexpress.stop_fetchmsg()