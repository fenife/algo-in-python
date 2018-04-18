# -*- coding: utf-8 -*-

"""
2.4.一个乱序字符串检查的例子

乱序字符串是指一个字符串只是另一个字符串的重新排列。
例如，'heart' 和 'earth' 就是乱序字符串。'python' 和 'typhon' 也是。

为了简单起见，我们假设所讨论的两个字符串具有相等的长度，并且他们由 26 个小写字母集合组成。

我们的目标是写一个布尔函数，它将两个字符串做参数并返回它们是不是乱序。
"""

from __future__ import print_function

import sys
import os
sys.path.extend([os.path.abspath('..')])

from tools.wraps import run_time


@run_time
def anagram_solution_1(s1, s2):
    """
    解法一：冒泡检查

    检查第一个字符串是不是出现在第二个字符串中，如果可以检验到每一个字符，
    那这两个字符串一定是乱序。

    可以通过用 None 替换字符来了解一个字符是否完成检查。

    但是，由于 Python 字符串是不可变的，所以第一步是将第二个字符串转换为列表。
    检查第一个字符串中的每个字符是否存在于第二个列表中，如果存在，替换成 None。

    T = O(n^2)
    """

    alist = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1

    return still_ok


@run_time
def anagram_solution_2(s1, s2):
    """
    解法二：排序和比较

    即使 s1,s2 不同，它们都是由完全相同的字符组成的。
    所以，我们按照字母顺序从 a 到 z 排列每个字符串，如果两个字符串相同，
    那这两个字符串就是乱序字符串。

    因为用到了 Python 自带的排序方法，这个也要算到算法复杂度中：
    T = O(nlogn)
    """
    if len(s1) != len(s2):
        return False

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    # return ''.join(alist1) == ''.join(alist2)

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


@run_time
def anagram_solution_3(s1, s2):
    """
    解法三：穷举法

    穷举所有可能性。对于乱序检测，我们可以生成 s1 的所有乱序字符串列表，
    然后查看是不是有 s2。

    算法复杂度： O(n!)
    """
    pass


@run_time
def anagram_solution_4(s1, s2):
    """
    解法四：计数和比较

    两个乱序字符串具有相同数目的字符。

    我们首先计算的是每个字母出现的次数。
    由于有 26 个可能的字符，我们就用 一个长度为 26 的列表，每个可能的字符占一个位置。

    每次看到一个特定的字符，就增加该位置的计数器。最后如果两个列表的计数器一样，
    则字符串为乱序字符串。

    O(n)
    """
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok


if __name__ == "__main__":
    print(anagram_solution_1('abcde', 'aabde'))
    print(anagram_solution_2('abcdehff', 'acbdffhe'))
    print(anagram_solution_4('abcdjhhhhhhhhsfjljsjfls', 'bacdjfdsjlfjslfjldkjf'))

