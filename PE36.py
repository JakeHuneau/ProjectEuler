def is_palindrome(n):
    if type(n) != str:
        n = str(n)
    return n == n[::-1]


def main():
    tot = 0
    for i in range(1, 1000001):
        if is_palindrome(i) and is_palindrome('{0:b}'.format(i)):
            tot += i
    print(tot)


if __name__ == '__main__':
    main()