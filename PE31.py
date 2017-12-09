# Make an array that has configuration [2$, 1$, 50p, 20p, 10p, 5p, 2p, 1p]
# Can solve linear equation: x1 + 2 x2 + 5 x3 + 10 x4 + 20 x5 + 50 x6 + 100 x7 + 200 x8 = 200 and find # of solutions
# Eliminate x8 and add 1 to final number of solutions:
# x1 + 2 x2 + 5 x3 + 10 x4 + 20 x5 + 50 x6 + 100 x7 = 200
# Can solve this dynamically

def total_curr(l):
    '''
    l must be tuple that is number of (2$, 1$, 50p, 20p, 10p, 5p, 2p, 1p)
    '''
    return 200 * l[0] + 100 * l[1] + 50 * l[2] + 20 * l[3] + 10 * l[4] + 5 * l[5] + 2 * l[6] + 1 * l[7]

def main():
    ways = 1
    for a in range(3):  # 100p
        for b in range(1 + (200 - 100 * a) // 50):  # 50p
            for c in range(1 + (200 - 100 * a - 50 * b) // 20):  # 20p
                for d in range(1 + (200 - 100 * a - 50 * b - 20 * c) // 10):  # 10p
                    for e in range(1 + (200 - 100 * a - 50 * b - 20 * c - 10 * d) // 5):  # 5p
                        for f in range(1 + (200 - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e)//2):  # 1p
                            ways += 1
    print(ways)


if __name__ == '__main__':
    main()