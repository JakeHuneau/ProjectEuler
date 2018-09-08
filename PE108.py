# 1/n - 1/x = 1/y => y = xn / (x-n) = -x + x^2/(x-n) so x^2 / (x-n) must be an integer, so I'll find all the factors
# to x^2. The solution will be the first x^2 with at least 998 factors. But they must be distinct, so I need the set of
# factors to be equal to


def num_divisors_square(n):
    res = 1
    red = n
    d = 2
    while d <= red:
        if d % 2 == 0 and d > 2:
            d += 1
        if d > 100:
            break
        exponent = 0
        while red % d == 0:
            exponent += 1
            red /= d
        res *= exponent + 1
        d += 1
    return res


n = 1
while True:
    divs = num_divisors_square(n*n)
    half = (divs + 1) / 2
    if half >= 1000:
        print(n)
        break
    n += 1