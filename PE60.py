import time

from util.primes import *


def main():
    primes = sieve_of_eratosthenes(10000, start=3)

    for p1 in primes:
        for p2 in primes:
            if is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1))):

                for p3 in primes:
                    if is_prime(int(str(p1) + str(p3))) and\
                            is_prime(int(str(p3) + str(p1))) and\
                            is_prime(int(str(p3) + str(p2))) and\
                            is_prime(int(str(p2) + str(p3))):

                        for p4 in primes:
                            if is_prime(int(str(p1) + str(p4))) and\
                                    is_prime(int(str(p4) + str(p1))) and\
                                    is_prime(int(str(p2) + str(p4))) and\
                                    is_prime(int(str(p4) + str(p2))) and\
                                    is_prime(int(str(p3) + str(p4))) and\
                                    is_prime(int(str(p4) + str(p3))):

                                for p5 in primes:
                                    if is_prime(int(str(p1) + str(p5))) and\
                                            is_prime(int(str(p5) + str(p1))) and\
                                            is_prime(int(str(p2) + str(p5))) and\
                                            is_prime(int(str(p5) + str(p2))) and\
                                            is_prime(int(str(p3) + str(p5))) and\
                                            is_prime(int(str(p5) + str(p3))) and\
                                            is_prime(int(str(p4) + str(p5))) and\
                                            is_prime(int(str(p5) + str(p4))):
                                        print(p1, p2, p3, p4, p5)
                                        print(p1+p2+p3+p4+p5)
                                        return 1


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time()-start)