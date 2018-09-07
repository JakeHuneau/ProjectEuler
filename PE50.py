from util.primes import *


def main():
    primes = sieve_of_eratosthenes(2000000)
    added_primes = [0]
    for p in primes:
        added_primes.append(added_primes[-1] + p)
        if added_primes[-1] > 1000000:
            break

    c = len(added_primes)
    terms = 1
    for i in range(c):
        for j in range(c - 1, i + terms, -1):
            n = added_primes[j] - added_primes[i]
            if j - i > terms and n in primes:
                terms, max_prime = j - i, n
                break

    print(max_prime)

if __name__ == '__main__':
    main()
