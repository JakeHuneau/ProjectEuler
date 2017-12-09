from functools import reduce


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def main():
    triangle = 0
    i = 2
    while True:
        triangle = sum(range(i))
        divisors = factors(triangle)
        if len(divisors) > 500:
            break
        i += 1
    print(triangle)

if __name__ == '__main__':
    main()