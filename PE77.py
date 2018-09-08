from Project_Euler import sieve_of_eratosthenes


def main():
    num = 2
    primes = sieve_of_eratosthenes(1000)

    while True:
        ways = [0] * (num + 1)
        ways[0] = 1
        for i in range(len(primes)):
            for j in range(primes[i], num+1):
                ways[j] += ways[j - primes[i]]
        if ways[num] > 5000:
            print(num)
            break
        num += 1

main()
