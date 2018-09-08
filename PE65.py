from fractions import Fraction


def build_frac(terms):
    new_term = 1 / Fraction(1 / terms[-1])
    for term in reversed(terms[1:-1]):
        new_term = Fraction(term + (1 / new_term))
    return Fraction(terms[0] + 1 / new_term)


def main():
    terms = [2, 1, 2]  # terms for e
    for i in range(2, 100):
        terms += [1, 1, i * 2]
        i += 1
    frac = build_frac(terms[:100])
    print(sum([int(i) for i in str(frac.numerator)]))


if __name__ == '__main__':
    main()
