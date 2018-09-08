import numpy as np


def inc(i, k):  # length i starting with k
    if increasing[i][k] != -1:
        return increasing[i][k]
    res = 0
    for j in range(k, 10):
        res += inc(i - 1, j)
    increasing[i][k] = res
    return res


def dec(i, k):
    if decreasing[i][k] != -1:
        return decreasing[i][k]
    res = 0
    for j in range(0, k+1):
        res += dec(i-1, j)

    decreasing[i][k] = res
    return res


increasing = np.full((111, 11), -1, dtype=np.int64)
decreasing = np.full((111, 11), -1, dtype=np.int64)
tot_len = 100
sum_inc = 0
sum_dec = 0

for i in range(1, 10):
    increasing[1][i] = 1
    decreasing[1][i] = 1

for i in range(1, 110):
    decreasing[i][0] = 1

for a in range(1, tot_len + 1):
    for b in range(1, 10):
        sum_inc += inc(a, b)
        sum_dec += dec(a, b)


doubles = 9 * tot_len
tot = sum_inc + sum_dec - doubles
print(tot)
