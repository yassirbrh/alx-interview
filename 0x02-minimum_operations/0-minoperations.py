#!/usr/bin/env python3
'''
    Method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
'''


def minOperations(n):
    '''
        minOperations: function
        @n: the number to check the fewest number of operations to achieve it.
        return: the fewest number of operations to achieve n.
    '''
    number_of_h = 1
    number_of_ops = 0
    copy_of_h = 0
    number_of_factors = 1
    while number_of_h < n:
        if number_of_h == 1 or n % number_of_h == 0:
            number_of_factors += 1
            number_of_ops += 1
            copy_of_h = number_of_h
        number_of_ops += 1
        number_of_h += copy_of_h
        if number_of_h == n and number_of_factors > 2:
            return number_of_ops
    return 0
