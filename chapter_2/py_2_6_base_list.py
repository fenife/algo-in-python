# -*- coding: utf-8 -*-

"""
2.6.列表

Python 内置数据结构 list 的性能分析
"""

from __future__ import print_function

import sys
import os
sys.path.extend([os.path.abspath('..')])

from tools.wraps import run_time


def test1():
    """
    拼接运算符'+'：O(n)
    T = O(n^2)
    """
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    """
    'append'：O(n)
    T = O(n)
    """
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


if __name__ == '__main__':
    from timeit import Timer
    t1 = Timer("test1()", "from __main__ import test1")
    print('concat', t1.timeit(number=10000), 'ms')

    t2 = Timer("test2()", "from __main__ import test2")
    print('append', t2.timeit(number=10000), 'ms')

    t3 = Timer("test3()", "from __main__ import test3")
    print('comprehension', t3.timeit(number=10000), 'ms')

    t4 = Timer("test4()", "from __main__ import test4")
    print('concat', t4.timeit(number=10000), 'ms')
