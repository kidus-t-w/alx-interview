#!/usr/bin/python3
"""
Define the isWinner function, which provides
a solution to the Prime Game problem.
"""


def primes(n):
    """Generate a list of prime numbers from 1 to n, inclusive.
        Args:
            n (int): The upper limit of the range. The range starts at 1.
    """

    prime = []
    s = [True] * (n + 1)
    for p in range(2, n + 1):
        if (s[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                s[i] = False
    return prime


def isWinner(x, nums):
    """
        Determines the winner of the Prime Game.
        Args:
            x (int): Number of rounds in the game.
            nums (list of int): List of upper limits for each round.
        Returns:
            str: The name of the winner (Maria or Ben),
            or None if no winner can be determined.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Ma = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Ma += 1
    if Ma > Ben:
        return 'Maria'
    elif Ben > Ma:
        return 'Ben'
    return None
