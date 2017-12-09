import time


def main():
    big_pand = 0
    for i in range(1, 10000):
        for j in range(1, 10):
            pand_str = ''
            for k in range(1, j):
                pand_str += str(i * k)
            if ''.join(sorted(pand_str)) == '123456789':
                if int(pand_str) > big_pand:
                    big_pand = int(pand_str)
    print(big_pand)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time()-start)