import time


def main():
    perimeter_solns = dict()
    for i in range(1, 1001):
        perimeter_solns[i] = 0

    for i in range(1, 900):
        for j in range(1, 900):
            perim = i + j + (i**2 + j**2) ** 0.5
            if perim <= 1000 and perim.is_integer():
                perimeter_solns[int(perim)] += 1

    most_soln = 0
    p=0
    for pair in perimeter_solns.items():
        if pair[1] > most_soln:
            most_soln = pair[1]
            p = pair[0]
    print(p)

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time()-start)