def main():
    pow_digs = set()
    for i in range(1, 10):
        for j in range(1, 25):
            if len(str(i ** j)) == j:
                pow_digs.add(i ** j)
    print(pow_digs)
    print(len(pow_digs))


if __name__ == '__main__':
    main()