# -*- coding: utf-8 -*-

"""
3.21 无序链表
"""

from __future__ import print_function


class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):
    """
    无序列表

    每个链表对象将维护对链表头部的单个引用
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def size(self):
        """遍历"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        """遍历查询该项是否存在"""
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        if self.is_empty():
            print("Can not remove item from a empty linked list.")
            return

        previous = None
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if not found:
            print("Not found")
            return

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def show(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()


def test_unordered_list():
    ll = UnorderedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)

    ll.remove(1)
    ll.remove(2)

    ll.show()


if __name__ == "__main__":
    test_unordered_list()



