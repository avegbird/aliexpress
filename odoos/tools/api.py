# -*- coding: utf-8 -*-

from functools import wraps


def synchronized(lock_attr='_lock'):
    def decorator(func):
        @wraps(func)
        def warper(self, *args, **kwargs):
            lock = getattr(self, lock_attr)
            try:
                lock.acquire()
                return func(self, *args, **kwargs)
            finally:
                lock.release()
        return warper
    return decorator
