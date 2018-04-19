# -*- coding: utf-8 -*-

"""
3.17 双端队列（Deque）的实现
"""

from __future__ import print_function


class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        self.items.pop(0)

    def add_rear(self, item):
        self.items.append(item)

    def remove_rear(self, item):
        self.items.pop()

    def size(self):
        return len(self.items)













