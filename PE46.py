from util.Primes import *


def find_smallest(all_comps, primes):
    for c in all_comps:
        has_prime = False
        for p in primes:
            if p < c:
                if (((c - p) / 2) ** 0.5).is_integer():
                    has_prime = True
        if not has_prime:
            return c


def main():
    primes = sieve_of_eratosthenes(1000000)
    P = is_prime_arr(1000000)
    comps = P
    comps[1] = True
    for i in range(0, 1000000, 2):
        comps[i] = True  # Composite odds are False
    all_comps = set()
    for i in range(len(comps)):
        if not comps[i]:
            all_comps.add(i)

    print(find_smallest(all_comps, primes))




if __name__ == '__main__':
    main()