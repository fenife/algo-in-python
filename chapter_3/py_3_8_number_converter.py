# -*- coding: utf-8 -*-

"""
3.8 十进制数转换为其他进制的数

通过用栈存放余数来实现
"""

from __future__ import print_function

from py_3_5_stack import Stack


def divide_by_2(dec_num):
    """
    十进制转换为二进制
    """
    rem_stack = Stack()

    while dec_num > 0:
        rem = dec_num % 2       # 取余数
        rem_stack.push(rem)     # 余数进栈
        dec_num = dec_num // 2  # 商

    bin_str = ""
    while not rem_stack.is_empty():
        bin_str = bin_str + str(rem_stack.pop())

    return bin_str


def test_divide_by_2():
    print(divide_by_2(42))


def base_converter(dec_num, base):
    """
    十进制 -> base 进制
    """
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_num > 0:
        rem = dec_num % base
        rem_stack.push(digits[rem])
        dec_num = dec_num // base

    new_str = ""
    while not rem_stack.is_empty():
        new_str = new_str + str(rem_stack.pop())

    return new_str


def test_base_converter():
    print(base_converter(25, 2))
    print(base_converter(30, 16))


if __name__ == "__main__":
    test_divide_by_2()
    test_base_converter()
