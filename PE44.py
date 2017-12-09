def pent_num(n):
    return int(n * (3 * n - 1) / 2)


def main():
    pents = [pent_num(i) for i in range(3000, 4000)]
    i = 1
    pents = set()
    while True:
        i += 1
        new_pent = pent_num(i)
        for pent in pents:
            if new_pent - pent in pents and new_pent - 2 * pent in pents:
                print(new_pent - 2 * pent)
                break
        pents.add(new_pent)


if __name__ == '__main__':
    main()