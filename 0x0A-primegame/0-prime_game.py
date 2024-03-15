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
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, isPrime in enumerate(primes, 1):
        if i == 1 or not isPrime:
            continue
        for y in range(i + i, n + 1, i):
            primes[y - 1] = False
    return primes


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

    for _, n in zip(range(x), nums):
        primesCount = len(list(filter(lambda x: x, primes[0: n])))
        result['Ben'] += primesCount % 2 == 0
        result['Maria'] += primesCount % 2 == 1

    if result['Ben'] == result['Maria']:
        return None
    return max(result, key=result.get)
