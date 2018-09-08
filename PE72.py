from Project_Euler import phi


def main():
    tot = 0
    for i in range(2, 1000001):
        tot += phi(i)
    print(tot)


main()
