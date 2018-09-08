"""
Functions concerning prime numbers
"""

import numpy as np
import random
from collections import defaultdict

from util.tools import factors


def prime_generator():
    """
    Generates prime numbers by tracking composite numbers

    Yields:
        prime numbers
    """
    composites = defaultdict(list)  # {composite: factor}
    candidate = 2

    while True:  # Run forever

        if candidate not in composites:  # Must be prime
            yield candidate
            composites[candidate * candidate].append(candidate)  # square it since this is known composite

        else:  # Has factors
            for c in composites[candidate]:
                composites[c + candidate].append(c)

            del composites[candidate]  # clear space

        candidate += 1


def sieve_of_eratosthenes(n: int) -> list:
    """
    Uses Sieve of Eratosthenes to calculate all prime numbers up to n

    Args:
        n (int): Calculate primes up to this

    Returns:
        (list) prime numbers
    """
    if n < 2:
        return []

    primes = [True] * (n+1)

    for x in range(3, int(np.sqrt(n))+1, 2):
        for y in range(3, (n//x)+1, 2):
            primes[(x*y)] = False

    return [2] + [i for i in range(3, n, 2) if primes[i]]


def is_prime_arr(n: int) -> list:
    """
    Uses Sieve of Eratosthenes to calculate list of primes up to n. Format is an array of length
    n that is True for prime index and False for non-prime.

    Args:
        n (int): Length of array

    Returns:
        (list) of length n that is true for prime indexes and false for non-primes
    """
    primes = sieve_of_eratosthenes(n)
    P = [False] * n
    for p in primes:
        P[p] = True
    return P


def prime_factors(n: int) -> set:
    """
    Gets a set of prime factors of n

    Args:
        n (int): number to factorize

    Returns:
        (set) of prime factors
    """
    P = is_prime_arr(n)
    facts = factors(n)
    prime_facts = set()
    for fact in facts:
        if P[fact]:
            prime_facts.add(fact)
        else:
            facts = facts | prime_factors(fact)
    return prime_facts


def is_prime(n: int) -> bool:
    """
    Checks if n is prime

    Args:
        n (int): number to check

    Returns:
        (bool) if n is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for a in range(3, int(n ** 0.5) + 1, 2):
        if n % a == 0:
            return False

    return True


def miller_rabin(n: int) -> bool:
    """
    Checks if n is prime using miller_rabin technique

    Args:
        n (int): number to check if prime

    Returns:
        (bool) if prime
    """
    if n == 1:
        return False
    if n <= 3:
        return True

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for r in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

