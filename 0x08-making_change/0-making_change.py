#!/usr/bin/python3
""" alx interview """


def makeChange(coins, total):
    """Calculates the minimum number of coins needed to make
     change for a given total,
    or -1 if it's impossible.

    Args:
        coins: A list of coin denominations (positive integers).
        total: The total amount of change to make (positive integer).

    Returns:
        The minimum number of coins needed, or -1 if it's impossible.
    """

    if total is None or total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 change requires 0 coins

    # Iterate through the DP table, considering each coin denomination
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total can be achieved with the given coins
    return dp[total] if dp[total] != float('inf') else -1
