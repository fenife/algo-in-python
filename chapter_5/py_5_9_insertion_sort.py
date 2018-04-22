# -*- coding: utf-8 -*-

"""
3.9 插入排序
"""

from __future__ import print_function


def insertion_sort(alist):
    """
    它始终在列表的较低位置维护一个排序的子列表。
    然后将每个新项 “插入” 回先前的子列表，使得排序的子列表称为较大的一个项。
    """
    for index in range(1, len(alist)):
        cur_val = alist[index]
        position = index

        while position > 0 and cur_val < alist[position - 1]:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = cur_val


def test_insertion_sort():
    alist = [54,26,93,17,77,31,44,55,20]
    insertion_sort(alist)
    print(alist)


if __name__ == "__main__":
    test_insertion_sort()

