"""
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?
"""
from util.tools import sum_of_digits


def pe16():
    print(sum_of_digits(2 ** 1000))


if __name__ == '__main__':
    pe16()