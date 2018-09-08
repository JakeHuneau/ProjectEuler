"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def pe6():
    sum_of_squares = sum(i * i for i in range(1, 101))
    square_of_sums = sum(range(1, 101)) ** 2
    print(square_of_sums - sum_of_squares)

if __name__ == '__main__':
    pe6()