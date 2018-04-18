# -*- coding: utf-8 -*-

"""
3.5 用 list 实现栈
"""

from __future__ import print_function


class Stack(object):
    """
    Completed implementation of a stack ADT
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        """
        Returns the top item from the stack but does not remove it.
        """
        # return self.items[len(self.items)-1]
        return self.items[-1]

    def size(self):
        return len(self.items)


def test_stack():
    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    s.pop()
    s.pop()
    print(s.size())


if __name__ == '__main__':
    test_stack()
