"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

:Thoughts:
Care about LCM. Use prime factorization. Multiple prime factorization together for each of the numbers in the range.
We want to use the greatest exponent of each prime for each number.
This can be determined by log(20)/log(p). So multiply all these together
"""
from math import log

def pe5():
    lcm = 1
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for p in primes:
        lcm *= p ** (int(log(20) / log(p)))
    print(lcm)

if __name__ == '__main__':
    pe5()