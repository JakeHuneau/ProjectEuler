from functools import reduce


def factors(n):
    return set(sorted(list((reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0))))))


def good_reduce(num, denom):
    num_factors = factors(num)
    denom_factors = factors(denom)
    common_factors = num_factors & denom_factors
    gcf = max(common_factors)
    return num // gcf, denom // gcf


def bad_reduce(num, denom):
    num = str(num)
    denom = str(denom)
    if num[0] == denom[0]:
        num = num[1]
        denom = denom[1]
    elif num[1] == denom[1]:
        num = num[0]
        denom = denom[0]
    elif num[0] == denom[1]:
        num = num[1]
        denom = denom[0]
    elif num[1] == denom[0]:
        num = num[0]
        denom = denom[1]
    else:
        num = denom = 10
    if int(num) != 0 and int(denom) != 0:
        num, denom = good_reduce(int(num), int(denom))
    else:
        num = denom = 0
    return num, denom


def main():
    running_num = 1
    running_denom = 1
    for num in range(10, 100):
        for denom in range(num+1, 100):
            red_num1, red_denom1 = good_reduce(num, denom)
            red_num2, red_denom2 = bad_reduce(num, denom)
            if red_num1 == red_num2 and red_denom1 == red_denom2 and num % 10 != 0 and denom % 10 != 0:
                running_num *= red_num1
                running_denom *= red_denom1
    print(good_reduce(running_num, running_denom))


if __name__ == '__main__':
    main()
