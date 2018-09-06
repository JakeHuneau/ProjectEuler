import time


def main():
    max_dig_sum = 0
    for a in range(1, 101):
        for b in range(1, 101):
            dig_sum = sum([int(d) for d in str(a ** b)])
            if dig_sum > max_dig_sum:
                max_dig_sum = dig_sum
    print(max_dig_sum)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
    