from util.Project_Euler import *


def func_set(func):
    i = 0
    func_set = []
    while func(i) < 10000:
        if func(i) >= 1000:
            func_set.append(func(i))
        i += 1
    return func_set


def overlaps(set1, set2):
    # for example: 1234 and 3456 overlap
    overlap_set = []
    for i in set1:
        end = str(i)[2:]
        for j in set2:
            if str(j)[:2] == end:
                overlap_set.append([i, j])
    return overlap_set


def is_cyclic(num1, num2):
    if str(num1)[2:] == str(num2)[:2]:
        return True
    else:
        return False


def main():
    tri_set = func_set(tri)  # all these are 4 digs
    sq_set = func_set(sq)
    penta_set = func_set(pent)
    hexa_set = func_set(hexa)
    hepta_set = func_set(hepta)
    oct_set = func_set(oct)











if __name__ == '__main__':
    main()