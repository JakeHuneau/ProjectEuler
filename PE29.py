def main():
    distinct_pows = set()
    for a in range(2, 101):
        for b in range(2, 101):
            distinct_pows.add(a**b)
    print(len(distinct_pows))


if __name__ == '__main__':
    main()