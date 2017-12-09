from itertools import permutations


def has_prop(n):
    prop = True
    if int(n[1:4]) % 2 != 0:
        prop = False
    if int(n[2:5]) % 3 != 0:
        prop = False
    if int(n[3:6]) % 5 != 0:
        prop = False
    if int(n[4:7]) % 7 != 0:
        prop = False
    if int(n[5:8]) % 11 != 0:
        prop = False
    if int(n[6:9]) % 13 != 0:
        prop = False
    if int(n[7:10]) % 17 != 0:
        prop = False
    return prop


def main():
    all_pans = permutations('1234567890')
    have_prop = []
    for pan in all_pans:
        if has_prop(''.join(pan)):
            have_prop.append(int(''.join(pan)))
    print(have_prop)
    print(sum(have_prop))


if __name__ == '__main__':
    main()
