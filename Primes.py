import numpy as np
from functools import reduce


def sieve_of_eratosthenes(n):
    """
    Uses Sieve of Eratosthenes to calculate all prime numbers up to n
    Parameters
    ----------
    n: (integer) Calculate primes up to this

    Returns
    -------
    primes: (list) list of prime numbers
    """
    if n <= 2:
        return []
    primes = [True] * (n+1)
    for x in range(3, int(np.sqrt(n))+1, 2):
        for y in range(3, (n//x)+1, 2):
            primes[(x*y)] = False

    return [2] + [i for i in range(3, n, 2) if primes[i]]


def is_prime_arr(n):
    """
    Uses Sieve of Eratosthenes to calculate list of primes up to n. Format is an array of length
    n that is True for prime index and False for non-prime.
    Parameters
    ----------
    n: Length of array

    Returns
    -------
    P: List of length n that is true for prime indexes and false for non-primes
    """
    primes = sieve_of_eratosthenes(n)
    P = [False] * n
    for p in primes:
        P[p] = True
    return P


def factors(n):
    return set(sorted(list((reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0)))))[1:-1])


def prime_factors(n):
    P = is_prime_arr(n)
    facts = factors(n)
    prime_facts = set()
    for fact in facts:
        if P[fact]:
            prime_facts.add(fact)
        else:
            facts = facts | prime_factors(fact)
    return prime_facts