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
    total_coins_number = 0
    while coins != []:
        max_coin = max(coins)
        coins.remove(max_coin)
        if max_coin > total:
            if len(coins) == 1:
                return -1
            continue
        total_coins_number += int(total / max_coin)
        total %= max_coin
    return total_coins_number
