def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)


def main():
    i = 644
    while True:
        if npf(i) == 4:
            i += 1
            if npf(i) == 4:
                i += 1
                if npf(i) == 4:
                    i += 1
                    if npf(i) == 4:
                        print(i - 3)
                        break

        i += 1


if __name__ == '__main__':
    main()