"""Find the sum of the digits in the number 100!"""
from util.tools import sum_of_digits
from math import factorial

def pe20():
    print(sum_of_digits(factorial(100)))

if __name__ == '__main__':
    pe20()