"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def biggest_prime_factors(n):
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            if n == 1:
                return i


def pe_3(n):
    print(biggest_prime_factors(n))


if __name__ == '__main__':
    pe_3(600851475143)
