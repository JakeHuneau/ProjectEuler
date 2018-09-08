# Using Farey Sequence


def main():
    count = 0
    ceil = 12000
    a = 1
    b = 3
    c = 4000
    d = 11999

    while (c, d) != (1, 2):
        count += 1
        j = (ceil + b) // d
        e = j * c - a
        f = j * d - b
        a = c
        b = d
        c = e
        d = f

    print(count)


main()
