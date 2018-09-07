from util.primes import sieve_of_eratosthenes


def main():
    primes = sieve_of_eratosthenes(2000000)
    print(sum(primes))


if __name__ == '__main__':
    main()