# -*- coding: utf-8 -*-

"""
4.10 汉诺塔游戏
"""

from __future__ import print_function


def move_disk(fp, tp):
    print("moving disk from", fp, "to", tp)


def move_tower(height, from_pole, to_pole, with_pole):
    """
    使用目标杆将 height-1 的塔移动到中间杆。
    将剩余的盘子移动到目标杆。
    使用起始杆将 height-1 的塔从中间杆移动到目标杆。

    对于问题N，如果N-1已经解决了，那么N是否很容易解决
    """
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)


if __name__ == "__main__":
    move_tower(3, 'F', 'T', 'W')

