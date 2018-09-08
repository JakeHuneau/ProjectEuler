'''
from time import time
from Project_Euler import all_factors, miller_rabin, sieve_of_eratosthenes


primes = sieve_of_eratosthenes(100000000)
t1 = time()
tot = 0
for p in primes:
    i = p - 1
    factors = all_factors(i)
    all_good = True
    for f in factors:
        if not miller_rabin(f + i // f):
            all_good = False
            break
    if all_good:
        tot += i

print(tot)
'''
def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i)**2 <= x:
            y += i
        i //= 2
    return y


def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def compute():
    LIMIT = 10 ** 8

    isprime = list_primality(LIMIT + 1)

    def is_prime_generating(n):
        return all(
            (n % d != 0 or isprime[d + n // d])
            for d in range(2, sqrt(n) + 1))

    ans = sum(n for n in range(LIMIT + 1)
              if isprime[n + 1] and is_prime_generating(n))
    return str(ans)


if __name__ == "__main__":
    print(compute())