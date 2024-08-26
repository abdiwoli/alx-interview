#!/usr/bin/python3
""" get the winner """


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a prime number game.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers where each integer represents the upper
                 limit for that round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    # Generate sieve of Eratosthenes for prime numbers
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False

    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Test cases
if __name__ == "__main__":
    nums = [0] * 10000
    for i in range(10000):
        nums[i] = i

    print("Winner: {}".format(isWinner(10000, nums)))
