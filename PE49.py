from Primes import *


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


def main():
    primes = sieve_of_eratosthenes(10000)
    for p in primes:
        p2 = p + 3330
        p3 = p + 6660
        if p2 in primes and p3 in primes and is_permutation(p, p2) and is_permutation(p, p3):
            print(p)
            print(str(p) + str(p2) + str(p3))


if __name__ == '__main__':
    main()