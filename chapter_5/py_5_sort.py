# -*- coding: utf-8 -*-

"""
排序算法集合
---------------

# 算法分析

## 输入：
- 最好情况：数组有序
- 平均情况：数组元素随机
- 最坏情况：数组逆序

## 时间复杂度：
- 比较
- 交换

## 空间复杂度

"""

from __future__ import print_function
from time import time


class BaseSort(object):
    def __init__(self, alist):
        self.alist = alist

    def sort(self):
        # 具体的算法未实现
        raise NotImplementedError

    @staticmethod
    def less(a, b):
        return a < b

    @staticmethod
    def exch(a, i, j):
        # 交换两个元素
        # a[i], a[j] = a[j], a[i]
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
        # assert self.isSorted()


class BubbleSort(BaseSort):
    """
    冒泡排序，升序排列

    外循环是遍历每个元素，每次都放置好一个元素
    内循环是比较相邻的两个元素，把大的元素交换到后面
    等到第一步中循环好了以后也就说明全部元素排序好了

    当前索引右边的所有元素都是有序的

    - 平均情况：
        比较： T = O((n^2)/2)
        交换： T = O((n^2)/2)
        总的： T = O(n^2)
    - 最好情况（已经排好序，不用交换）：
        比较： T = O((n^2)/2)
        交换： T = 0
        总的： T = O(n^2)
    - 最坏情况（逆序）：
        > 每一次排序都要交换两个元素
        > 比上面最优的情况所花的时间就是在于交换元素的三个步骤
        比较： T = O((n^2)/2)
        交换： T = [ 3n(n-1) ] / 2
        总的： T = O(n^2)
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

        - 最好情况：
            > 一趟比较下来，发现都是排好序的，标志一直是 False ，
            > 则直接退出循环，表示排序完成
            T = O(n)
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

    - 平均：
        : 平均情况下，每个元素都可能向后移动半个数组的长度
        比较：O((n^2)/4)
        交换：O((n^2)/4)
    - 最好：
        : 所有元素都不需要移动位置
        : 每插入一个元素，只需要考查前一个元素
        比较：O(n)
        交换：0
    - 最坏：
        : 每个元素都需要移动位置
        比较：O((n^2)/2)
        交换：O((n^2)/2)

    """
    def sort(self):
        self.insertion_sort()

    def insertion_sort(self):
        a = self.alist
        n = len(a)
        for i in range(n):
            # 将 a[i] 插入到 a[i-1], a[i-2], ... a[0] 之中
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    self.exch(a, j, j-1)


class ShellSort(BaseSort):
    """
    希尔排序 - 基于插入排序

    交换不相邻的元素以对数组的局部进行排序，并最终用插入排序将局部有序的数组进行排序

    希尔排序的思想是：使数组中任意间隔为 h 的元素都是有序的。
    这样的数组被称为： h 有序子数组

    实现：对于每个 h ，用插入排序将 h 个子数组独立的排序；
    只要在插入排序的代码中将移动元素的距离有 1 改为 h 即可

    希尔排序更高效的原因：权衡了子数组的规模和有序性

    算法的性能也取决间隔 h ，这里的递增序列为： h = 3*h + 1

    大概的复杂度：T = O[n^(3/2)] < O(n^2)
    """
    def sort(self):
        self.shell_sort()

    def shell_sort(self):
        a = self.alist
        n = len(a)
        h = 1
        while h < n // 3:
            h = 3*h + 1     # 1, 4, 13, 40, 121, 364, ...

        while h >= 1:       # 将数组变为 h 有序
            for i in range(h, n):
                # 将 a[i] 插入到 a[i-h], a[i-2*h], a[i-3*h], ... 之中
                for j in range(i, h-1, -h):         # j=i, j>=h, j=j-h
                    if a[j] < a[j-h]:               # j-h >= 0, j>=h
                        self.exch(a, j, j-h)
            h = h // 3


class MergeSort(BaseSort):
    """
    归并排序

    """
    def sort(self):
        self.merge_sort()

    def merge_sort(self):
        a = self.alist
        n = len(a)




if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 9]
    # s = BubbleSort(alist)
    # s = SelectionSort(alist)
    # s =InsertionSort(alist)
    s = ShellSort(alist)
    s.test()

