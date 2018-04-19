# -*- coding: utf-8 -*-

"""
3.13 模拟：烫手山芋

假设拿着山芋的孩子在队列的前面。当拿到山芋的时候，这个孩子将先出列再入队列，
把他放在队列的最后。经过 num 次的出队入队后，前面的孩子将被永久移除队列。
并且另一个周期开始，继续此过程，直到只剩下一个名字（队列的大小为 1）。
"""

from __future__ import print_function
from py_3_12_queue import Queue


def hot_potato(name_list, num):
    """

    :param name_list:
    :param num:
    """
    queue = Queue()

    for name in name_list:
        queue.enqueue(name)

    while queue.size() > 1:
        # 经过 num 次的出队入队后，前面的项将被永久移除队列
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()


def test_hot_potato():
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


if __name__ == "__main__":
    test_hot_potato()

