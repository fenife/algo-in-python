# -*- coding: utf-8 -*-

"""
5.12 快速排序
"""

from __future__ import print_function


def partition(alist, first, last):
    pivot_val = alist[first]    # 选择分区点的值
    le = first + 1              # 从左边开始的 index
    ri = last                   # 从右边开始的 index
    done = False

    while not done:
        # 右标变得小于左标记的点时，停止循环
        while le <= ri and alist[le] <= pivot_val:
            # 增加左标记，直到找到一个大于区分点的值
            le = le + 1

        while le <= ri and alist[ri] >= pivot_val:
            # 递减右标，直到找到小于区分点的值
            ri = ri - 1

        if le > ri:
            done = True
        else:
            # 交换
            alist[le], alist[ri] = alist[ri], alist[le]

    # 右标记的位置现在是分割点，交换分割点与 first 点的值，区分点的值现在就位
    alist[first], alist[ri] = alist[ri], alist[first]

    # 返回区分点的 index
    return ri


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)

        quick_sort_helper(alist, first, split_point-1)
        quick_sort_helper(alist, split_point+1, last)


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def test_quick_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist)
    print(alist)


if __name__ == "__main__":
    test_quick_sort()





