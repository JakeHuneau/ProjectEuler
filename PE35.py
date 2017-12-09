from Primes import sieve_of_eratosthenes


def get_rotations(n):
    n_list = [i for i in str(n)]
    all_rotations = {n}
    for i in range(1, len(n_list)):
        rotation = n_list[i:] + n_list[:i]
        rotation_int = int(''.join(rotation))
        all_rotations.add(rotation_int)
    return all_rotations


def main():
    primes = sieve_of_eratosthenes(1000000)
    P = [False] * 1000000
    for p in primes:
        P[p] = True

    circular_primes = []
    for p in primes:
        all_rotations = get_rotations(p)
        circular = True
        for i in all_rotations:
            if not P[i]:
                circular = False
        if circular:
            circular_primes.append(p)
    print(circular_primes)
    print(len(circular_primes))


if __name__ == '__main__':
    main()