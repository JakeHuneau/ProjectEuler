"""
Numbers that can be represented by a regular geometrical arrangement of equally spaced points

http://mathworld.wolfram.com/FigurateNumber.html
"""

def tri(n):
    return int(n * (n + 1) / 2)


def sq(n):
    return n ** 2


def pent(n):
    return int(n * (3 * n - 1) /2)


def hexa(n):
    return int(n * (2*n - 1))


def hepta(n):
    return int(n * (5*n - 3) /2)


def oct(n):
    return int(n * (3 * n - 2))


def is_tri(n):
    return (((1 + 8*n) ** 0.5 -1)/2).is_integer()


def is_square(n):
    return (n ** 0.5).is_integer()


def is_pent(n):
    return ((1 + (1 + 24 * n) ** 0.5) / 6).is_integer()


def is_hexa(n):
    return ((1 + (1 + 24*n) ** 0.5) / 4).is_integer()


def is_hepta(n):
    return ((3 + (9 + 40*n) ** 0.5) / 10).is_integer()


def is_oct(n):
    return ((2 + (4 + 12*n) ** 0.5) / 6).is_integer()