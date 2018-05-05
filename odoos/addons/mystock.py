# -*- coding: utf-8 -*-
import threading
from odoos.tools import api
from time import time


class MyStock(object):

    def __init__(self, maxsize=2):
        # 栈最大长度
        self.maxsize = maxsize
        # 栈
        self.stock = []
        # 线程锁
        self._lock = threading.Lock()
        # 非空锁 当栈不为空时唤醒线程
        self.not_empty = threading.Condition(self._lock)
        # 非满锁 当栈不满时唤醒线程
        self.not_full = threading.Condition(self._lock)
        # 任务全部结束锁
        self.all_tasks_done = threading.Condition(self._lock)
        # 未结束任务个数
        self.unfinished_tasks = 0
        # 是否去重
        self.distinct = False

    def task_done(self):
        self.all_tasks_done.acquire()
        try:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all()
            self.unfinished_tasks = unfinished
        finally:
            self.all_tasks_done.release()

    def join(self):
        self.all_tasks_done.acquire()
        try:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()
        finally:
            self.all_tasks_done.release()

    @api.synchronized()
    def ssize(self):
        # 当前栈长度
        return self._ssize()

    @api.synchronized()
    def empty(self):
        # 当前栈是否为空
        return not self._ssize()

    @api.synchronized()
    def full(self):
        # 栈是否已满
        return 0 < self.maxsize == self._ssize()

    def put(self, item, block=True, timeout=None):
        """
        向栈加入元素
        :param item:
        :param block: 栈满时是否等待
        :param timeout: 过时时间
        :return:
        """
        self.not_full.acquire()
        try:
            if self.maxsize > 0:
                if not block:
                    if self._ssize() == self.maxsize:
                        raise ValueError("栈已满")
                elif timeout is None:
                    while self._ssize() == self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._ssize() == self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise ValueError("栈已满")
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()
        finally:
            self.not_full.release()

    def put_list(self, item, block=True, timeout=None):
        """
        向栈加入列表元素
        :param item:
        :param block: 栈满时是否等待
        :param timeout: 过时时间
        :return:
        """
        self.not_full.acquire()
        try:
            if self.maxsize > 0:
                if not block:
                    if self._ssize() == self.maxsize:
                        raise ValueError("栈已满")
                elif timeout is None:
                    while self._ssize() == self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._ssize() == self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise ValueError("栈已满")
                        self.not_full.wait(remaining)
            for i in item:
                self._put(i)
            self.unfinished_tasks += 1
            self.not_empty.notify()
        finally:
            self.not_full.release()

    def get(self, block=True, timeout=None):
        """
        获取元素
        :param block: 空时是否等待
        :param timeout: 过时时间
        :return:
        """
        self.not_empty.acquire()
        try:
            if not block:
                if not self._ssize():
                    raise ValueError("栈为空")
            elif timeout is None:
                while not self._ssize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._ssize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise ValueError("栈为空")
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item
        finally:
            self.not_empty.release()

    def get_list(self, num, block=True, timeout=None):
        """
        获取元素
        :param num: 获取数量
        :param block: 空时是否等待
        :param timeout: 过时时间
        :return:
        """
        self.not_empty.acquire()
        try:
            if not block:
                if not self._ssize():
                    raise ValueError("栈为空")
            elif timeout is None:
                while not self._ssize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._ssize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise ValueError("栈为空")
                    self.not_empty.wait(remaining)
            if self._ssize() < num:
                res = [] + self.stock
                self.stock = []
            else:
                res = [] + self.stock[self._ssize() - num:]
                self.stock = self.stock[:self._ssize() - num]
            self.not_full.notify()
            return res
        finally:
            self.not_empty.release()

    def _ssize(self):
        return len(self.stock)

    def _put(self, item):
        if self.distinct:
            if item not in self.stock:
                self.stock.append(item)
        else:
            self.stock.append(item)

    def _get(self):
        return self.stock.pop()

