# -*- coding: utf-8 -*-

"""
5.10 希尔排序
"""

from __future__ import print_function


def shell_sort(alist):
    """
    通过将原始列表分解为多个较小的子列表来改进插入排序，
    每个子列表使用插入排序进行排序。 选择这些子列表的方式是希尔排序的关键。
    不是将列表拆分为连续项的子列表，希尔排序使用增量i（有时称为 gap），
    通过选择 i 个项的所有项来创建子列表。

    从 n/2 子列表开始。下一次，n/4 子列表排序。
    最后，单个列表按照基本插入排序进行排序。
    """
    sub_list_count = len(alist) // 2
    while sub_list_count > 0:
        for start in range(sub_list_count):
            gap_insertion_sort(alist, start, sub_list_count)

        print("After increments of size", sub_list_count,
              ", The list is", alist)
        sub_list_count = sub_list_count // 2


def gap_insertion_sort(alist, start, gap):
    """
    当 gap = 1 时，就是插入排序
    """

    for i in range(start + gap, len(alist), gap):
        cur_val = alist[i]
        position = i

        while position >= gap and alist[position - gap] > cur_val:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = cur_val


def test_shell_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    shell_sort(alist)
    print(alist)


if __name__ == "__main__":
    test_shell_sort()




