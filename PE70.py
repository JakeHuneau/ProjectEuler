from Project_Euler import *
import time


def main():
    min_totient = 100
    n_min = 1
    for i in range(2, 10000000):
        totient = phi(i)
        if is_permutation(i, totient):
            if i / totient < min_totient:
                min_totient = i / totient
                n_min = i
    print(n_min)
    print(min_totient)


if __name__ == '__main__':
    s = time.time()
    main()
    print(time.time()-s)
