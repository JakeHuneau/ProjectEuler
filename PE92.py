def add_square(n):
    return sum(map(lambda x: x**2, [int(s) for s in str(n)]))


def end_in_89(n):
    while True:
        n = add_square(n)
        if n == 89:
            return True
        if n == 1:
            return False


c = 0
dict89 = dict()

for i in range(1, 568):  # All possible numbers
    dict89[i] = end_in_89(i)

for i in range(1, 10000000):
    if dict89[add_square(i)]:
        c += 1

print(c)
