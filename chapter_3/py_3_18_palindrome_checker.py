# -*- coding: utf-8 -*-

"""
3.18 回文检查

回文是一个字符串，读取首尾相同的字符，例如，radar、toot、madam
"""

from __future__ import print_function
from py_3_17_deque import Deque


def pal_checker(string):
    deque = Deque()

    for ch in string:
        deque.add_rear(ch)

    still_equal = True

    while deque.size() > 1 and still_equal:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal


def test_pal_checker():
    print(pal_checker('lsdkjfskf'))
    print(pal_checker('radar'))


if __name__ == "__main__":
    test_pal_checker()









