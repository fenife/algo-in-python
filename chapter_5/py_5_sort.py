# -*- coding: utf-8 -*-

"""

"""

from __future__ import print_function
from time import time


class BaseSort(object):
    def __init__(self, alist):
        self.alist = alist

    def sort(self):
        raise NotImplementedError

    @staticmethod
    def less(a, b):
        return a < b

    @staticmethod
    def exch(a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    def show(self):
        print(self.alist)

    def isSorted(self):
        a = self.alist
        for i in range(len(a)-1):
            if not self.less(a[i], a[i+1]):
                return False
        return True

    def test(self):
        print('-'*5, self.__class__.__name__, '-'*5)
        print("Before sort:", self.alist)
        start = time()
        self.sort()
        end = time()
        print("After  sort:", self.alist)
        print("run time:", end - start)
        assert self.isSorted()


class BubbleSort(BaseSort):
    """
    冒泡排序，升序排列

    当前索引右边的所有元素都是有序的
    """
    def sort(self):
        # self.short_bubble_sort()
        self.bubble_sort_3()

    def bubble_sort(self):
        a = self.alist
        n = len(a)
        for i in range(n):                 # 表示 n 次排序过程
            for j in range(1, n-i):        # 后面的 i 项已经排好序，所以不用再比较
                if a[j-1] > a[j]:          # 前面的数字大于后面的数字就交换
                    self.exch(a, j-1, j)   # 交换a[j-1]和a[j]

    def bubble_sort_2(self):
        a = self.alist
        n = len(a) - 1
        for i in range(n, 0, -1):           # i 逐次减少
            for j in range(i):              # 同上，后面的 n-i 项已经排好序
                if a[j] > a[j+1]:
                    self.exch(a, j, j+1)

    def bubble_sort_3(self):
        a = self.alist
        n = len(a) - 1
        while n > 0:
            for j in range(n):
                if a[j] > a[j+1]:
                    self.exch(a, j, j+1)
            n = n - 1

    def short_bubble_sort(self):
        """
        优化：

        如果对于一个本身有序的序列，或则序列后面一大部分都是有序的序列，
        上面的算法就会浪费很多的时间开销

        设置一个标志，如果这一趟发生了交换，则为true，否则为false。
        明显如果有一趟没有发生交换，说明排序已经完成。
        """
        a = self.alist
        n = len(a) - 1
        exchange = True
        while n > 0 and exchange:
            exchange = False
            for j in range(n):
                if a[j] > a[j+1]:
                    exchange = True
                    self.exch(a, j, j+1)
            n = n - 1


class SelectionSort(BaseSort):
    """
    选择排序，升序排列

    当前索引左边的所有元素都是有序的

    比较次数：O((n^2)/2)
        - 运行时间和输入无关，无论输入的数据元素是有序的或随机的

    交换次数：O(n)
        - 相对与其他算法，数据移动是最少的
    """
    def sort(self):
        self.selection_sort()

    def selection_sort(self):
        a = self.alist
        n = len(a)      # 列表、数组长度

        # 表示 n 次排序过程，第 i 次排序 第 i 大的元素
        # 有多少个元素，就有多少次排序过程
        for i in range(n):
            # 将 a[i] 和 a[i+1 ... n] 中最小的元素交换
            min = i         # 最小元素的索引
            for j in range(i+1, n):
                if a[j] < a[min]:
                    min = j

            self.exch(a, i, min)


class InsertionSort(BaseSort):
    """
    插入排序，升序排列

    当前索引左边的所有元素都是有序的，但是它们的最终位置还不确定，
    为了给更小的元素腾出空间，它们可能会被移动。当索引到达数组右边时，
    排序就完成了

    排序时间取决于输入中元素的初始顺序

    """
    def sort(self):
        self.insertion_sort()

    def insertion_sort(self):
        a = self.alist
        n = len(self.alist)



if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 9]
    s = BubbleSort(alist)
    # s = SelectionSort(alist)
    s.test()

