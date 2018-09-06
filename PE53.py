from math import factorial


def num_combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def main():
    counter = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if num_combinations(n, r) > 1000000:
                counter += 1
    print(counter)


if __name__ == '__main__':
    main()