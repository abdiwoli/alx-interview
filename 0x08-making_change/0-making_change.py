#!/usr/bin/python3
""" alx interview """


def makeChange(coins, total):
    """Calculates the minimum number
     of coins needed to make change for a given total,
    or -1 if it's impossible, using a list comprehension with map.

    Args:
        coins: A list of coin denominations (positive integers).
        total: The total amount of change to make (positive integer).

    Returns:
        The minimum number of coins needed, or -1 if it's impossible.
    """

    if total is None or total <= 0:
        return 0

    # Create a list of possible change amounts using map
    possible_changes = [min(dp[i - coin] + 1,
                            float('inf')) for coin in coins for i in range(1,
                                                                           total + 1)]

    # Find the minimum number of coins (filter for finite values)
    min_coins = min(filter(lambda x: x != float('inf'), possible_changes))

    return min_coins if min_coins != float('inf') else -1
