import time
from itertools import product

from util.primes import *


def all_locations(num_spots):
    # For example: for num_spots = 3, we have ###. So we can have *##, **#, *#*, #*#, #**, ##*
    # Return set of tuples of len = num_spots with T/F values
    locs = []
    for i in product([True, False], repeat=num_spots):
        if not all(i):
            locs.append(i)
    return locs


def find_all_replacements(n):
    n_str = str(n)
    all_replacements = []
    replacement_locs = all_locations(len(n_str))
    for i in replacement_locs:
        curr_config = set()
        for n in range(10):
            curr_str = [s for s in n_str]
            for j in range(len(i)):
                if i[j]:
                    curr_str[j] = str(n)
            curr_config.add(int(''.join(curr_str)))
        all_replacements.append(curr_config)
    return all_replacements


def main():
    primes = sieve_of_eratosthenes(1000000)
    P = is_prime_arr(1000000)
    for p in primes:
        all_p_rep = find_all_replacements(p)
        for p2 in all_p_rep:
            counter = 0
            rep_primes = []
            for p3 in p2:
                if P[p3] and len(str(p3)) == len(str(p)):
                    rep_primes.append(p3)
                    counter += 1
            if counter == 8:
                print(min(rep_primes))
                return(p)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
