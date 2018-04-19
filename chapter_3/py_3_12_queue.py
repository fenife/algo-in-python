# -*- coding: utf-8 -*-

"""
3.10 队列的实现
"""

from __future__ import print_function


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def test_queue():
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    print(q.is_empty())
    print(q.size())
    print(q.dequeue())


if __name__ == "__main__":
    test_queue()


