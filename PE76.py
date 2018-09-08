#Pretty much like that currency problem. Dynamic solution

def main():
    num_way = [0] * 101
    num_way[0] = 1

    for i in range(1, 100):
        for j in range(i, 101):
            num_way[j] += num_way[j - i]

    print(num_way[100])

main()