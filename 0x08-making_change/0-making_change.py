#!/usr/bin/python3
'''
    Function makeChange that takes a list of coins and returns the fewest
    number of coins needed to meet a given amount total.
'''


def makeChange(coins, total):
    '''
        makeChange: function
        @coins: The list of coins.
        @total: The total to achieve.
        return: The fewest number of coins.
    '''
    if total <= 0:
        return 0
    remain_total = total
    total_coins_number = 0
    sorted_coins = sorted(coins, reverse=True)
    i = 0
    while remain_total > 0:
        if i >= len(sorted_coins):
            return -1
        max_coin = sorted_coins[i]
        if max_coin > remain_total:
            if i == len(sorted_coins) - 1:
                return -1
            i += 1
            continue
        total_coins_number += int(remain_total / max_coin)
        remain_total %= max_coin
        i += 1
    return total_coins_number
