#!/usr/bin/python3
'''
    Function isWinner that returns the name of the player winning the most
    in prime game.
'''


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    '''
        isWinner: function
        @x: Number of the rounds.
        @nums: List of numbers.
        return: name of the player winning the most.
    '''
    if x < 1 or not nums:
        return None
    num_rounds = x
    i = 0
    result = {'Ben': 0, 'Maria': 0}
    while num_rounds:
        elem = nums[i]
        opponent = 'Ben'
        for j in range(2, elem + 1):
            if is_prime(j):
                if opponent == 'Ben':
                    opponent = 'Maria'
                else:
                    opponent = 'Ben'
        result[opponent] += 1
        i += 1
        num_rounds -= 1
    if result['Ben'] == result['Maria']:
        return None
    return max(result, key=result.get)
