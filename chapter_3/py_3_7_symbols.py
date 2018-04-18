# -*- coding: utf-8 -*-

"""
3.6 符号匹配
"""

from __future__ import print_function

# import the Stack class as previously defined
from py_3_5_stack import Stack


def par_checker(symbol_string):
    """
    检查符号'([{'、')]}'是否匹配
    """
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

    # return True if balanced and s.is_empty() else False


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


def test_par_checker():
    print(par_checker('{{([][])}()}'))
    print(par_checker('[{()]'))
    print(par_checker('[{()}]'))


if __name__ == '__main__':
    test_par_checker()



