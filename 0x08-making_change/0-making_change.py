#!/usr/bin/python3

""" Make change"""


def makeChange(coins, total):
    """
    Returns the minimum number of coins needed to meet the total.

    Args:
        coins (list): A list of coin values.
        total (int): The total value to be met.

    Returns:
        int: The minimum number of coins needed to meet the total.
            Returns -1 if the total is less than or equal to zero.
            Returns -1 if the total cannot be met by any number of coins.

    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
