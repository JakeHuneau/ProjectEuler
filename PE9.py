def berggren_alg(a, b, c):
    """
    Calculates the next set of three Pythagorean triples using Berggren's algorithm that three new sets can be
    calculated with:
    |  | new side a | new side b | new side c |
    |T1| a- 2b + 2c |2a - b + 2c |2a - 2b + 3c|
    |T2| a + 2b + 2c|2a + b + 2c |2a + 2b + 3c|
    |T3|-a + 2b + 2c|-2a + b + 2c|-2a +2b + 3c|
    Parameters
    ----------
    a: (int) original a
    b: (int) original b
    c: (int) original c

    Returns
    -------
    new_triples: (list) list of three tuples that are new Pythagorean triples
    """
    trip1 = tuple(sorted([a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c]))
    trip2 = tuple(sorted([a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c]))
    trip3 = tuple(sorted([-1 * a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c]))
    trip4 = tuple(sorted([2 * a + b - c, -2 * a + 2 * b + 2 * c, -2 * a + b + 3 * c]))
    trip5 = tuple(sorted([2 * a + b + c, 2 * a - 2 * b + 2 * c, 2 * a - b + 3 * c]))
    trip6 = tuple(sorted([2 * a - b + c, 2 * a + 2 * b + 2 * c, 2 * a + b + 3 * c]))
    return trip1, trip2, trip3, trip4, trip5, trip6


def pythagorean_triples(n):
    """
    Calculates Pythagorean triples (a^2 + b^2 = c^2) where c<=n
    Parameters
    ----------
    n: (int) upper limit for c

    Returns
    -------
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


def main():
    for num in range(1, 1000):
        for dig in range(num, 1000 - num):
            i = 1000 - num - dig
            if num ** 2 + dig ** 2 == i ** 2:
                print(num, dig, i)
                print(num * dig * i)


if __name__ == '__main__':
    main()

