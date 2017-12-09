# Use Fermat's little theorem and prime fact that decimal expansion of 1/p is periodic with period length equal to
# e = order of 10 modulo p: e is smallest pos int such that 10^e is equiv 1 (mod p)
from Primes import sieve_of_eratosthenes

def main():
    possible_nums = sieve_of_eratosthenes(1000)[::-1]
    longest_decimal = 0
    d = 0
    while True:
        for p in possible_nums:
            local_longest_dec = 1
            while (10 ** local_longest_dec) % p != 1:
                local_longest_dec += 1
            if local_longest_dec > longest_decimal:
                longest_decimal = local_longest_dec
                d = p
            if longest_decimal == p - 1:
                break
        break

    print(longest_decimal, d)


if __name__ == '__main__':
    main()