# Diagonals for side length (odd) s: s^2, s^2 - 3(s+1), s^2 - 2(s+1), s^2 - (s+1)


import time

from util.primes import is_prime


def main():
    num_primes = 0
    num_diags = 1
    s = 3
    while True:
        if is_prime(s ** 2 - 3 * s + 3):
            num_primes += 1
        if is_prime(s ** 2 - 2 * s + 2):
            num_primes += 1
        if is_prime(s ** 2 - s + 1):
            num_primes += 1

        num_diags += 4

        if num_primes / num_diags < .1:
            print(s)
            return num_primes / num_diags

        s += 2

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
