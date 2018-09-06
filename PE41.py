from util.Primes import *


def is_pandigital(n, upto=9):
    comp = ''
    for i in range(1, upto+1):
        comp += str(i)
    if ''.join(sorted(str(n))) == comp:
        return True
    else:
        return False


def main():
    while True:
        for p in sieve_of_eratosthenes(10000000)[::-1]:
            if is_pandigital(p, len(str(p))):
                print(p)
                break


if __name__ == '__main__':
    main()