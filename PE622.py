from Project_Euler import factors
from time import time


def get_lens(x):
    return [1 + i for i in factors(2**x - 1)]


def get_mins(x):
    lower_mins = set()
    t1 = time()
    for i in range(1, x):
        lower_mins = lower_mins.union(set(get_lens(i)))
        print(f'got {i} in {time()-t1} s')
    return set(get_lens(x)).difference(lower_mins)


print(sum(get_mins(60)))