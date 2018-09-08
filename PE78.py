from Project_Euler import *
from time import time


def main():
    k = pentagonal_arr(500)

    p, sgn, n, m = [1], [1, 1, -1, -1], 0, 1000000

    while p[n] > 0:
        n += 1
        px, i = 0, 0
        while k[i] <= n:
            px += p[n - k[i]] * sgn[i % 4]
            i += 1
        p.append(px % m)

    print(n)

s = time()
main()
print(time()-s)
