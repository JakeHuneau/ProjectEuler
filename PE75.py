from math import gcd


def main():
    max = 1500000
    triangles = [0] * (max + 1)
    count = 0
    floor = int((max / 2) ** 0.5)

    for i in range(2, floor):
        for j in range(1, i):
            if (i + j) % 2 == 1 and gcd(i, j) == 1:
                a = i ** 2 + j ** 2
                b = i ** 2 - j ** 2
                c = 2 * i * j
                p = a + b + c
                while p <= max:
                    triangles[p] += 1
                    if triangles[p] == 1:
                        count += 1
                    if triangles[p] == 2:
                        count -= 1
                    p += a + b + c
    print(count)


main()