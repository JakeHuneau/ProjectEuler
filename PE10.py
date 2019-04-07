"""
Find the sum of all the primes below two million.
"""

from util.primes import sieve_of_eratosthenes


def pe10():
    primes = sieve_of_eratosthenes(2000000)
    print(sum(primes))


if __name__ == '__main__':
    pe10()
