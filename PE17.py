def num_str(num):
    return [int(i) for i in str(num)]


def count_ones(int):
    if int in (1, 2, 6):
        return 3
    elif int in (4, 5, 9):
        return 4
    elif int in (3, 7, 8):
        return 5
    else:
        return 0


def count_tens(tens, ones):
    if tens == 1:
        if ones in (1, 2):
            return 6
        elif ones in (3, 4):
            return 8
        elif ones == 5:
            return 7
        else:
            return 4 + count_ones(ones)
    if tens in (2, 3, 4, 8, 9):
        return 6 + count_ones(ones)
    elif tens in (5, 6):
        return 5 + count_ones(ones)
    elif tens == 7:
        return 7 + count_ones(ones)
    else:
        return count_ones(ones)


def count_hundreds(hundreds, tens, ones):
    if hundreds == 0:
        return 3
    else:
        if tens == 0 and ones == 0:
            return 7 + count_ones(hundreds)
        else:
            return 7 + 3 + count_ones(hundreds)


def count_thousands(thousands):
    return 8 + count_ones(thousands)


def main():
    tot_len = 0
    for i in range(1, 1001):
        num_str_list = num_str(i)[::-1]
        if len(num_str_list) == 1:
            tot_len += count_ones(num_str_list[0])
        elif len(num_str_list) == 2:
            tot_len += count_tens(num_str_list[1], num_str_list[0])
        elif len(num_str_list) == 3:
            tot_len += count_hundreds(num_str_list[2], num_str_list[1], num_str_list[0])
            tot_len += count_tens(num_str_list[1], num_str_list[0])
        elif len(num_str_list) == 4:
            tot_len += count_thousands(num_str_list[3])

    print(tot_len)
    print(count_tens(3,1))



if __name__ == '__main__':
    main()
