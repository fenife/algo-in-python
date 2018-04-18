# -*- coding: utf-8 -*-

"""
一些有用的装饰器
"""

from __future__ import print_function

from time import time


def run_time(f):
    def wrapper(*args, **kwargs):
        start = time()
        re = f(*args, **kwargs)
        end = time()
        print("'%s' run time: %e" % (f.__name__, end - start))

        return re

    return wrapper
