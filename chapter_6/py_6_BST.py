# -*- coding: utf-8 -*-

"""
二叉查找树
"""

from __future__ import print_function


class Node(object):
    def __init__(self, key, value, n):
        self.key = key      # 键
        self.val = value    # 值
        self.left = None    # 指向左边子树的链接
        self.right = None   # 指向右边子树的链接
        self.N = n          # 以该节点为根的子树中的结点总数


class BST(object):
    """
    二叉查找树
    """
    def __init__(self, root):
        self.root = root

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        return 0 if x is None else x.N

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        """
        查找

        在以 x 为根结点的子树中查找并返回 key 所对应的值

        :param x:   Node x
        :param key: key
        :return:    key -> val
        """
        if x is None:
            return None

        if key < x.key:
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        """
        插入

        如果 key 存在于以 x 为根结点的子树中则更新它的值；
        否则将以 key 和 val 为键值对的新结点插入到该子树中

        :param x:   Node x
        :param key:
        :param val:
        :return:    Node x
        """
        if x is None:
            return Node(key, val, 1)

        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val

        x.N = self._size(x.left) + self._size(x.right) + 1
        return x



