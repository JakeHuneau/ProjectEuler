from itertools import permutations


def add_ring(outter, inner):
    inner = inner * 2
    sums = []
    for i in range(len(outter)):
        sums.append(outter[i] + sum(inner[i:i+2]))
    return sums


def main():
    all_possible = [list(p) for p in permutations([i for i in range(1, 11)])]
    max_set = 0
    for i in all_possible:
        outter = i[:len(i) // 2]
        inner = i[len(i) // 2:]

        while outter[0] != min(outter):
            outter = outter[1:] + outter[:1]
            inner = inner[1:] + inner[:1]

        ring_sums = add_ring(outter, inner)
        if len(set(ring_sums)) == 1:
            inner = inner * 2
            sol_seq = []
            for j in range(len(outter)):
                sol_seq.append(outter[j])
                sol_seq.append(inner[j])
                sol_seq.append(inner[j+1])
            set_val_str = ''.join([str(k) for k in sol_seq])
            if len(set_val_str) == 16:
                set_val = int(set_val_str)
                if set_val > max_set:
                    max_set = set_val
    print(max_set)


if __name__ == '__main__':
    main()