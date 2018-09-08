from Project_Euler import sieve_of_eratosthenes


def main():
    max_n = 1
    for p in sieve_of_eratosthenes(100):
        if max_n * p > 1000000:
            print(max_n)
            return 1
        max_n *= p


if __name__ == '__main__':
    main()