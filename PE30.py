def sum_of_fifths(n):
    return sum([int(s)**5 for s in str(n)])


def main():
    fifth_nums = []
    for i in range(2, 1000000):
        if i == sum_of_fifths(i):
            fifth_nums.append(i)
    print(fifth_nums)
    print(sum(fifth_nums))


if __name__ == '__main__':
    main()
