#!/usr/bin/python3
'''
    Function isWinner that returns the name of the player winning the most
    in prime game.
'''


def SieveOfEratosthenes(n):
    """
    Generates a list of prime numbers up to n using the Sieve of Eratosthenes
    algorithm.
    """
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]


def isWinner(x, nums):
    '''
        isWinner: function
        @x: Number of the rounds.
        @nums: List of numbers.
        return: name of the player winning the most.
    '''
    if x < 1 or not nums:
        return None

    result = {'Ben': 0, 'Maria': 0}
    primes = SieveOfEratosthenes(max(nums))

    for elem in nums:
        opponent = 'Ben'
        for j in range(2, elem + 1):
            if j in primes:
                opponent = 'Maria' if opponent == 'Ben' else 'Ben'
        result[opponent] += 1

    if result['Ben'] == result['Maria']:
        return None
    return max(result, key=result.get)
