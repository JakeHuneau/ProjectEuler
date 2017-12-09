# Spiral is 1001 x 1001, so starts at 1001^2
# Start at top number then add n - (999 + 1) 4 times
# Then add n - (997 + 1) 4 times
# continue until - 1


def main():
    square_dim = 1001
    total = square_dim ** 2
    current_num = total
    i = square_dim - 2
    while i > 0:
        for j in range(4):
            current_num -= (i + 1)
            total += current_num
        i -= 2
    print(total)


if __name__ == '__main__':
    main()