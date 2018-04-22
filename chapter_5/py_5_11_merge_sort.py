# -*- coding: utf-8 -*-

"""
5.11 归并排序
"""

from __future__ import print_function


def merge_sort(alist):
    """
    归并排序是一种递归算法，不断将列表拆分为一半。
    如果列表为空或有一个项，则按定义（基本情况）进行排序。
    如果列表有多个项，我们分割列表，并递归调用两个半部分的合并排序。
    一旦对这两半排序完成，就执行合并操作。
    合并是获取两个较小的排序列表并将它们组合成单个排序的新列表的过程。

    O(nlog^n)
    """
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        # print("left ", left_half)
        # print("right ", right_half
        # 合并，通过重复从排序列表中取最小的项目，将项目逐个放回切分后的原始列表（alist）。
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1
            k = k + 1

        # 合并左边的剩余部分
        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1

        # 合并右边的剩余部分
        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merging ", alist)


def test_merge_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    merge_sort(alist)
    print(alist)


if __name__ == "__main__":
    test_merge_sort()




