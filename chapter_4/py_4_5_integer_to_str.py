# -*- coding: utf-8 -*-

"""
4.5 整数转换为任意进制字符串
"""

from __future__ import print_function


def to_str(n, base):
    conv_str = "0123456789ABCDEF"
    if n < base:
        return conv_str[n]
    else:
        return to_str(n//base, base) + conv_str[n % base]


if __name__ == "__main__":
    print(to_str(1453, 10))
    print(to_str(10, 2))

