"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

There exists one Pythagorean triple for which a + b + c = 1000. Find the product a*b*c

:Thoughts:
Berggren's algorithm
"""
from util.algorithms import berggren_alg


def pythagorean_triples(n):
    """
    Calculates Pythagorean triples (a^2 + b^2 = c^2) where c<=n

    args:
        n: (int) upper limit for c

    returns:
        py_triples: (list) list of Pythagorean triples in the form (a,b,c)
    """
    trips = [(3, 4, 5)]
    i = 0
    while True:
        new_trips = trips[i]
        a, b, c = new_trips[0], new_trips[1], new_trips[2]
        if c <= n:
            trip1, trip2, trip3, trip4, trip5, trip6 = berggren_alg(a, b, c)

            if trip1 not in set(trips):
                trips.append(trip1)
            if trip2 not in set(trips):
                trips.append(trip2)
            if trip3 not in set(trips):
                trips.append(trip3)
            if trip4 not in set(trips):
                trips.append(trip4)
            if trip5 not in set(trips):
                trips.append(trip5)
            if trip6 not in set(trips):
                trips.append(trip6)

        if i >= len(trips)-1:
            break

        else:
            i += 1

    return trips


def pe9():
    for num in range(1, 1000):
        for dig in range(num, 1000 - num):
            i = 1000 - num - dig
            if num ** 2 + dig ** 2 == i ** 2:
                print(num, dig, i)
                print(num * dig * i)


if __name__ == '__main__':
    pe9()

