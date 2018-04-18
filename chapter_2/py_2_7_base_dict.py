# -*- coding: utf-8 -*-

"""
2.7.列表

Python 内置数据结构 dict 的性能分析
"""

from __future__ import print_function

import timeit
import random
import sys
import os
sys.path.extend([os.path.abspath('..')])


# def compare_contain_op_of_list_and_dict():
if __name__ == "__main__":
    """
    比较 list 和 dict 之间的 contains(in) 操作的性能
    """
    for i in range(10000, 1000001, 20000):
        t = timeit.Timer("random.randrange(%d) in x" % i,
                         "from __main__ import random, x")
        x = list(range(i))
        lst_time = t.timeit(number=1000)

        x = {j: None for j in range(i)}
        dst_time = t.timeit(number=1000)

        print("%d, %10.3f, %10.3f" % (i, lst_time, dst_time))



