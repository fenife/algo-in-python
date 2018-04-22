# -*- coding: utf-8 -*-

"""
5.5 实现 HashTable (map)
"""

from __future__ import print_function


class HashTable(object):
    """
    slots 的列表将保存键项
    data 的并行列表将保存数据值
    当我们查找一个键时，data 列表中的相应位置将保存相关的数据值
    """
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def rehash(self, old_hash, size):
        """
        冲突解决：`加1` 的线性探测
        """
        return (old_hash + 1) % size

    def hash_func(self, key, size):
        """
        计算 hash 值
        """
        return key % size

    def put(self, key, data):
        """
        计算原始哈希值，如果该槽不为空（出现冲突），则迭代 rehash 函数，直到出现空槽
        如果非空槽已经包含 key，则旧数据值将替换为新数据值
        """
        hash_value = self.hash_func(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data    # replace
            else:
                # 找到下一个空槽
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and \
                        self.slots[hash_value] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data     # replace

    def get(self, key):
        """
        从计算初始哈希值开始。如果值不在初始槽中，则 rehash 用于定位下一个可能的位置
        """
        start_slot = self.hash_func(key, len(self.slots))
        data = None
        found = False
        stop = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def test():
    H = HashTable()
    H[31] = 'hello'
    H[20] = 'world'
    H[20] = 'python'
    print(H.data)


def test_hash_table():
    H = HashTable()
    H[30] = 'hello'
    H[20] = 'world'

    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    H[20] = 'duck'
    print(H.slots)
    print(H.data)


if __name__ == "__main__":
    test_hash_table()
    # test()










