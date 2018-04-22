# -*- coding: utf-8 -*-

"""
5.8 选择排序
"""

from __future__ import print_function


def selection_sort(alist):
    """
    选择排序在他遍历时寻找最大的值，并在完成遍历后，将其放置在正确的位置。
    与冒泡排序一样，在第一次遍历后，最大的项在正确的地方。 第二遍后，下一个最大的就位。
    """
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



