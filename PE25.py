def F(m, n):
    return m + n

def main():
    i = 3
    f0 = 1
    f1 = 1
    while True:
        oldf1 = f1
        f1 = F(f1, f0)
        f0 = oldf1
        if len(str(f1)) >= 1000 or i == 1000000:
            print(i)
            break
        else:
            i += 1


if __name__ == '__main__':
    main()