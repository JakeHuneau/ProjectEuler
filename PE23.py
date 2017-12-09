from functools import reduce


def factors(n):
    return set(sorted(list((reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0)))))[:-1])


def is_abundant(n):
    return sum(factors(n)) > n


def main():
    abundants = []
    for i in range(2, 28123):
        if is_abundant(i):
            abundants.append(i)

    sums = set()
    for x in abundants:
        for y in abundants:
            pair_sum = x + y
            if pair_sum < 28123:
                sums.add(pair_sum)

    all_nums = set(range(28123))
    diffs = all_nums - sums
    print(sum(diffs))


if __name__ == '__main__':
    main()
