# -*- coding: utf-8 -*-

"""
4.3 计算整数列表和
"""

from __future__ import print_function


def list_sum(num_list):
    """
    计算整数列表的总和
    不使用递归解决
    """
    sum = 0
    for num in num_list:
        sum = sum + num
    return sum


def list_sum_recursion(num_list):
    """
    计算整数列表的总和
    使用递归解决
    eg:
        sum = (1 + (3 + (5 + (7 + 9))))
    """
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])


if __name__ == "__main__":
    print(list_sum([1, 2, 3, 4, 5]))
    print(list_sum_recursion([1, 2, 3, 4, 5]))

