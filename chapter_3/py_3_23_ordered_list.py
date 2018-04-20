# -*- coding: utf-8 -*-

"""
3.23 有序链表
"""

from __future__ import print_function

from py_3_21_linked_list import Node


class OrderedList(object):
    """
    有序链表
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """遍历，同无序链表"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def add(self, item):
        """
        需要在现有的有序列表中查找新项所属的特定位置

        遍历链表，寻找添加新节点的地方

        当我们迭代完节点（ current 变为 None）或 current 节点的值大于
        我们希望添加的项时，我们就找到了该位置。
        """
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        tmp = Node(item)
        if previous is None:
            tmp.set_next(self.head)
            self.head = tmp
        else:
            tmp.set_next(current)
            previous.set_next(tmp)

    def search(self, item):
        """
        遍历查询该项是否存在

        因为链表是有序的，如果发现任何节点包含大于我们正在寻找的项的数据，
        我们将 stop 设置为 True ，结束搜索

        其余行与无序列表搜索相同
        """
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def remove(self, item):
        """删除节点，同无序链表"""
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


def test_ordered_list():
    ll = OrderedList()
    ll.add(2)
    ll.add(1)
    ll.add(3)

    ll.remove(1)
    # ll.remove(2)

    ll.show()


if __name__ == "__main__":
    test_ordered_list()






