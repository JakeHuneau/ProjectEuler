"""
A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

:Thoughts:
Just brute force.
"""

from util.classifications import is_palindrome

def pe_4():
    biggest = 0
    for i in range(900, 1000):
        for j in range(900, 1000):
            num = i * j
            if is_palindrome(num) and num > biggest:
                biggest = num
    print(biggest)

if __name__ == '__main__':
    pe_4()