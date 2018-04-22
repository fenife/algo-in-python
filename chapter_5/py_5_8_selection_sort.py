# -*- coding: utf-8 -*-

"""
5.8 选择排序
"""

from __future__ import print_function


def selection_sort(alist):
    for fill_slot in range(len(alist)-1, 0, -1):
        position_of_max = 0
        for i in range(1, fill_slot+1):
            if alist[i] > alist[position_of_max]:
                position_of_max = i

        alist[fill_slot], alist[position_of_max] = alist[position_of_max], alist[fill_slot]


def test_selection_sort():
    alist = [54,26,93,17,77,31,44,55,20]
    selection_sort(alist)
    print(alist)


if __name__ == "__main__":
    test_selection_sort()



