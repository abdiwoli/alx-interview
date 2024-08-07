#!/usr/bin/python3
""" get teh winner """


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a prime number game.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers where each integer represents the upper

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
    """
    def is_prime(num):
        """
        Checks if a given number is prime.

        Parameters:
        num (int): The number to check for primality.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to(n):
        """
        Generates a list of all prime numbers up to a given number

        Parameters:
        n (int): The upper limit for finding prime numbers.

        Returns:
        list: A list of prime numbers up to and including n.
        """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
        for start in range(2, int(n**0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, n + 1, start):
                    sieve[multiple] = False
        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def play_game(n):
        """
        Simulates a round of the prime number game and determines the winner.

        Parameters:
        n (int): The upper limit of the set of consecutive integers

        Returns:
        str: The name of the player who wins the game ("Maria" or "Ben").
        """
        if n < 2:
            return "Ben"

        primes = get_primes_up_to(n)
        primes_set = set(primes)
        turn = 0  # Maria's turn
        while primes_set:
            prime = min(primes_set)
            multiples = {prime * i for i in range(1, n // prime + 1)}
            primes_set -= multiples
            turn += 1
        return "Maria" if turn % 2 == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
