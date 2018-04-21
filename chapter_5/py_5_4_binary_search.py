# -*- coding: utf-8 -*-

"""
5.4 二分查找
"""

from __future__ import print_function


def binary_search(alist, item):
    """
    二分查找从中间项开始，而不是按顺序查找列表。
    如果该项是我们正在寻找的项，我们就完成了查找。
    如果我们正在查找的项大于中间项，就可以消除中间项以及比中间项小的一半元素。
    如果该项在列表中，肯定在大的那半部分。
    然后我们可以用大的半部分重复这个过程。
    从中间项开始，将其与我们正在寻找的内容进行比较。
    再次，我们找到元素或将列表分成两半，消除可能的搜索空间的另一部分。
    """
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def test_binary_search():
    alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(alist, 3))
    print(binary_search(alist, 13))


def rec_binary_search(alist, item):
    """
    递归方式实现二分查找

    # O(k) 是 list 切片所需的时间
    O(log^n) + O(k)
    """
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return rec_binary_search(alist[:mid], item)
        else:
            return rec_binary_search(alist[mid+1:], item)


def test_rec_binary_search():
    alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(rec_binary_search(alist, 3))
    print(rec_binary_search(alist, 13))


if __name__ == "__main__":
    # test_binary_search()
    test_rec_binary_search()

