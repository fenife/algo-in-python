# -*- coding: utf-8 -*-

"""
3.14 模拟：打印机

平均每天大约10名学生在任何给定时间在实验室工作。这些学生通常在此期间打印两次，
这些任务的长度范围从1到20页。实验室中的打印机较旧，每分钟以草稿质量可以处理10页。
打印机可以切换以提供更好的质量，但是它将每分钟只能处理五页。较慢的打印速度可能会
使学生等待太久。应使用什么页面速率？

如果实验室中有 10 个学生，每人打印两次，则平均每小时有 20 个打印任务。
在任何给定的秒，打印任务将被创建的时机是什么？ 回答这个问题的方法是考虑任务与时间的比率。
每小时 20 个任务意味着平均每 180 秒将有一个任务。
"""

from __future__ import print_function
import random
from py_3_12_queue import Queue


class Printer(object):
    def __init__(self, ppm):
        self.page_rate = ppm        # 打印速率，每分钟多少页
        self.current_task = None    # 当前打印任务
        self.time_remaining = 0     # 任务剩余时间

    def tick(self):
        if self.current_task:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        # if self.current_task:
        #     return True
        # else:
        #     return False
        return True if self.current_task else False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task(object):
    """
    Task 类表示单个打印任务。

    创建任务时，随机数生成器将提供 1 到 20 页的长度。

    每个任务还需要保存一个时间戳用于计算等待时间。此时间戳将表示任务被创建
    并放置到打印机队列中的时间。
    """
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        # 检索在任务打印开始之前在队列中花费的时间
        return current_time - self.timestamp


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(num_seconds, page_per_minute):
    """
    模拟：当前打印机是否可以处理任务负载

    new_print_task 决定是否创建一个新的打印任务。
    我们再次选择使用随机模块的 randrange 函数返回 1 到 180 之间的随机整数。
    打印任务每 180 秒到达一次。通过从随机整数的范围中任意选择来模拟这个随机事件。

    模拟功能允许我们设置打印机的总时间和每分钟的页数。

    :param num_seconds:     运行模拟多少秒
    :param page_per_minute: 打印机每分钟打印的页数
    """
    lab_printer = Printer(page_per_minute)
    print_queue = Queue()
    waiting_times = []

    for curent_second in range(num_seconds):
        if new_print_task():
            task = Task(curent_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(curent_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def test_simulation():
    # 进行 10 次独立试验
    # 每次使用每分钟五页的页面速率运行模拟 60 分钟（3,600秒）
    for i in range(10):
        simulation(3600, 10)


if __name__ == "__main__":
    test_simulation()





