from util.primes import *


def get_all_truncs(n):
    truncs = {n}
    str_n = [i for i in str(n)]
    for i in range(1, len(str_n)):
        trunc_f = str_n[i:]
        trunc_b = str_n[:i]
        trunc_f_int = int(''.join(trunc_f))
        trunc_b_int = int(''.join(trunc_b))
        truncs.add(trunc_b_int)
        truncs.add(trunc_f_int)
    return truncs


def main():
    primes = sieve_of_eratosthenes(1000000)
    P = is_prime_arr(1000000)
    trunc_primes = []
    for p in primes:
        truncs = get_all_truncs(p)
        trunc_prime = True
        for trunc in truncs:
            if not P[trunc]:
                trunc_prime = False
        if trunc_prime:
            trunc_primes.append(p)
    trunc_primes = trunc_primes[4:]
    print(trunc_primes)
    print(len(trunc_primes))
    print(sum(trunc_primes))


if __name__ == '__main__':
    main()
