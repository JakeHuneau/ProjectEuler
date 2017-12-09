def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def main():
    n = 600851475143
    return largest_prime_factor(n)


if __name__ == '__main__':
    print(main())
