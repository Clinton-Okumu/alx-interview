#!/usr/bin/python3
"""In a text file, there is a single character H."""


def minOperations(n):
    """Calculates the fewest number of operations needed"""

    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
