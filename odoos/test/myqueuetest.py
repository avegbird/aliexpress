# -*- coding: utf-8 -*-
from odoos.addons import mystock
import threading
import time

myq = mystock.MyStock(10)
num = [1, 2, 3, 4, 5]

def target1():
    global num
    while True:
        myq.put_list(num)
        for i in num:
            i += 1
        time.sleep(0.1)


def target2(i):
    while True:
        print i, myq.get_list(5)
        time.sleep(0.2)


for i in range(10):
    threading.Thread(target=target2, args=[i]).start()
threading.Thread(target=target1).start()
