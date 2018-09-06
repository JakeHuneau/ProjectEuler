from util.Primes import sieve_of_eratosthenes


def quad(a, b, n):
    return n ** 2 + a * n + b


def prime_bool_arr(n):
    primes = sieve_of_eratosthenes(n)
    prime_bools = [False] * n
    for p in primes:
        prime_bools[p] = True
    return prime_bools


def main():
    prime_bools = prime_bool_arr(1000000)
    max_n = 0
    max_a = 0
    max_b = 0
    for a in range(-1000, 1000):
        for b in range(1, 1000):
            n = 0
            while True:
                if n > max_n:
                    max_n = n
                    max_a = a
                    max_b = b
                if prime_bools[quad(a, b, n)] == True:
                    n += 1
                else:
                    break
    print(max_a, max_b, max_n)
    print(max_a * max_b)



if __name__ == '__main__':
    main()