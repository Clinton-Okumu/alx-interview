#!/usr/bin/python3
"""
A function to determine the fewest number of coins needed to meet a given total.
"""

def makeChange(coins, total):
    """
    Function to calculate the fewest number of coins needed to make a given total.

    Arguments:
    coins -- list of coin values
    total -- the total value to be made

    Returns:
    The minimum number of coins needed to make the total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

