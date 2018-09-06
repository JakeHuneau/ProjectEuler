from itertools import permutations
import time


def perm_mults(n):
    perms = [int(''.join(i)) for i in permutations(str(n))]
    mults = set()
    for perm in perms:
        if (perm / n).is_integer():
            mults.add(perm // n)
    return sorted(list(mults))


def main():
    i = 125874
    while True:
        if perm_mults(i) == [1, 2, 3, 4, 5, 6]:
            print(i)
            return i
        i += 1


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
