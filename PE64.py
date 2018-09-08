# Using https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

def next_coeff(S, an, dn, mn):
    mm = dn * an - mn
    dm = (S - mm ** 2) // dn
    a0 = int(S ** 0.5)
    am = int((a0 + mm) / dm)
    return am, dm, mm


def get_sqrt_seq_len(S):
    m0 = 0
    d0 = 1
    a0 = int(S ** 0.5)
    sqrt_seq = [a0]
    period = 0

    while a0 != 2 * int(S ** 0.5):
        a0, d0, m0 = next_coeff(S, a0, d0, m0)
        sqrt_seq.append(a0)
        period += 1
    return sqrt_seq, period


def main():
    count = 0
    for i in range(2, 10001):
        if not (i ** 0.5).is_integer():
            sqrt_seq = get_sqrt_seq_len(i)
            if sqrt_seq[1] & 1 == 1:
                count += 1
    print(count)


if __name__ == '__main__':
    main()