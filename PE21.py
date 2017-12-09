from functools import reduce
import time


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def factor_sum(n):
    return sum(sorted(list(factors(n)))[:-1])


def is_amicable(n):
    factor_sum1 = factor_sum(n)
    factors_sum2 = factor_sum(factor_sum1)
    return factors_sum2 == n and factor_sum1 != n


def main():
    amicable_nums = []
    for i in range(2, 10000):
        if is_amicable(i):
            amicable_nums.append(i)
    print(amicable_nums)
    print(sum(amicable_nums))


if __name__ == '__main__':
    t1 = time.time()
    main()
    print(time.time() - t1)