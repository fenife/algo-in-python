# -*- coding: utf-8 -*-

"""
红黑树
"""

from __future__ import print_function

RED = True
BLACK = False


class Node(object):
    def __init__(self, key, value, n, color):
        self.key = key      # 键
        self.val = value    # 值
        self.left = None    # 指向左边子树的链接
        self.right = None   # 指向右边子树的链接
        self.N = n          # 以该节点为根的子树中的结点总数
        self.color = color  # 由其父节点指向它的链接的颜色


class RedBlackBST(object):
    """
    二叉查找树
    """
    def __init__(self, root):
        self.root = root

    def is_red(self, x):
        return False if x is None else x.color == RED

    def rotate_left(self, h):
        """
        左旋转

        :param h:   Node h
        :return:    Node
        """
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self._size(h.left) + self._size(h.right)
        return x

    def rotate_right(self, h):
        """
        右旋转

        :param h:   Node h
        :return:    Node
        """
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self._size(h.left) + self._size(h.right)
        return x

    def flip_colors(self, h):
        """
        颜色转换

        :param h:   Node h
        """
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

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
        self.root.color = BLACK

    def _put(self, x, key, val):
        """
        插入

        如果 key 存在于以 x 为根结点的子树中则更新它的值；
        否则将以 key 和 val 为键值对的新结点插入到该子树中

        如果右子结点是红色的而左子结点是黑色的，进行左旋转；
        如果左子结点是红色的且它的左子结点也是红色的，进行右旋转；
        如果左右子结点均为红色，进行颜色转换

        :param x:   Node x
        :param key:
        :param val:
        :return:    Node x
        """
        if x is None:
            return Node(key, val, 1, RED)

        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val

        if self.is_red(x.right) and not self.is_red(x.left):
            x = self.rotate_left(x)

        if self.is_red(x.left) and self.is_red(x.left.left):
            x = self.rotate_right(x)

        if self.is_red(x.left) and self.is_red(x.right):
            self.flip_colors(x)

        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def show(self):
        self._show(self.root)

    def _show(self, x):
        if x is None:
            return
        self._show(x.left)
        print(x.key, x.val)
        self._show(x.right)


