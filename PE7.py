"""
What is the 10 001st prime number?

:Thoughts:
Use a prime generator
"""
from util.primes import prime_generator

def pe7():
    p = 0
    prime = prime_generator()
    for i in range(10001):
        p = next(prime)
    print(p)

if __name__ == '__main__':
    pe7()
