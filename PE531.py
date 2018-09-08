from Project_Euler import memoize
from sympy.ntheory import factorint


@memoize
def prime_factors(n):
    prime_dict = factorint(n)
    prime_facts = list(prime_dict.keys())
    return prime_facts


@memoize
def phi(n):
    """
    Euler totient function. Number of positive integers up to n that are relatively prime to n
    Parameters
    ----------
    n

    Returns
    -------

    """
    pf = prime_factors(n)
    prod = n
    for p in pf:
        prod *= (1 - 1/p)
    return int(prod)


@memoize
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def g(a, n, b, m):
    b1, n0, m0 = xgcd(a, b)
    if a > b:
        s0 = b + (a - b)*m0*m
        if s0 > 0:
            return s0
        else:
            return 0
    elif b > a:
        s0 = a + (b - a)*n0*n
        if s0 > 0:
            return s0
        else:
            return 0
    else:
        return 0


tot = 0
start, stop = 1000000, 1005000
for n in range(start, stop):
    for m in range(n+1, stop):
        tot += g(phi(n), n, phi(m), m)

print(tot)

#4515432351156203105