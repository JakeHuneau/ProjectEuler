
def main():
    with open('names.txt', 'r') as data:
        names_str = data.read()
    names_list = sorted(names_str.split(','))
    i = 1
    total = 0
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for name in names_list:
        name = name.strip('"')
        name_total = 0
        for letter in name:
            name_total += letters.index(letter) + 1
        total += i * name_total
        i += 1
    print(total)


if __name__ == '__main__':
    main()