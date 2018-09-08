from collections import defaultdict


def main():
    cubes = defaultdict(list)
    i = 1
    while True:
        c = i ** 3
        digits = ''.join(sorted([d for d in str(c)]))
        cubes[digits].append(c)

        for cube_list in cubes.values():
            if len(cube_list) == 5:
                return min(cube_list)

        i += 1


if __name__ == '__main__':
    print(main())
