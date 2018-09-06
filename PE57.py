from time import time
from fractions import Fraction


def sqrt2_frac(iters):
    frac = Fraction(3, 2) # First iteration
    for i in range(iters):
        frac = Fraction(1 + 1 / (1 + frac))
    return frac

def main():
    count = 0
    for i in range(1000):
        frac = sqrt2_frac(i)
        if len(str(frac.numerator)) > len(str(frac.denominator)):
            count += 1
    print(count)


if __name__ == '__main__':
    start = time()
    main()
    print(time()-start)