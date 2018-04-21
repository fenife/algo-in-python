# -*- coding: utf-8 -*-

"""
4.12 动态规划
"""

from __future__ import print_function


def rec_mc(coin_value_list, change):
    """
    使用最少的硬币找零

    num_coins = min(
        1+num_coins(original_amount−1)
        1+num_coins(original_amount−5)
        1+num_coins(original_amount−10)
        1+num_coins(original_amount−25)
    )
    """
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_mc(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


def rec_dc(coin_value_list, change, known_results):
    """
    通过缓存优化

    将最小数量的硬币的结果存储在表中，从而避免重新计算我们已经知道的结果
    """
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        # 检查已经计算过的列表中是否包含此找零的最小硬币数量
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_dc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins

    return min_coins


def dp_make_change(coin_value_list, change, min_coins, coin_used):
    """
    动态规划算法

    跟踪使用的硬币

    :param coin_value_list: 一个有效硬币值的列表
    :param change: 需要找零的额度
    :param min_coins: 包含每个值所需最小硬币数量的列表
    :param coin_used: 用于找零的硬币的列表
    """
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for i in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents-i] + 1 < coin_count:
                coin_count = min_coins[cents-i] + 1
                new_coin = i

        min_coins[cents] = coin_count
        coin_used[cents] = new_coin
    return min_coins[change]


def print_coins(coin_used, change):
    coin = change
    while coin > 0:
        this_coin = coin_used[coin]
        print(this_coin)
        coin = coin - this_coin


def test_dp_make_change():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coin_used = [0] * (amnt + 1)
    coin_count = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dp_make_change(clist, amnt, coin_count, coin_used), "coins")
    print("They are:")
    print_coins(coin_used, amnt)
    print("The used list is as follows:")
    print(coin_used)


if __name__ == "__main__":
    # print(rec_mc([1, 5, 10, 25], 63))
    # print(rec_dc([1, 5, 10, 25], 63, [0]*64))
    # print(dp_make_change([1, 5, 10, 25], 63, [0]*64))
    test_dp_make_change()







