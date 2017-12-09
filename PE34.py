def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact


def main():
    cur_nums = []
    for i in range(3, 100000):
        broken_num = [int(j) for j in str(i)]
        sum_fact = sum([factorial(j) for j in broken_num])
        if sum_fact == i:
            cur_nums.append(i)
    print(cur_nums)
    print(sum(cur_nums))


if __name__ == '__main__':
    main()