#!/usr/bin/python3
""" alx interview """
from collections import deque


def makeChange(coins, amount):
    """ make change """
    if amount is None or amount == 0:
        return 0
    # Queue will store tuples of (current_amount, number_of_coins)
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            new_amount = current_amount + coin
            if new_amount == amount:
                return num_coins + 1
            if new_amount < amount and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))

    return -1
