# -*- coding: utf-8 -*-

"""
5.7 冒泡排序
"""

from __future__ import print_function


def bubble_sort(alist):
    """
    冒泡排序需要多次遍历列表。它比较相邻的项并交换那些无序的项。
    每次遍历列表将下一个最大的值放在其正确的位置。
    每个项“冒泡”到它所属的位置。
    """
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def test_bubble_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(alist)
    print(alist)


def short_bubble_sort(alist):
    """
    短冒泡排序

    对于只需要遍历几次列表，冒泡排序具有识别排序列表和停止的优点
    如果发现列表已排序，可以修改冒泡排序提前停止
    """
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1


def test_short_bubble_sort():
    alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 90]
    short_bubble_sort(alist)
    print(alist)


if __name__ == "__main__":
    # test_bubble_sort()
    test_short_bubble_sort()