def factorial(n):
    f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return f[n]


def factsum(n):
    return sum([factorial(int(i)) for i in str(n)])


def fact_chain(n):
    broken = factsum(n)
    chain = [n, broken]
    while factsum(broken) not in chain:
        broken = factsum(broken)
        chain.append(broken)
    return chain


def main():
    max = 1000000
    count = 0
    lengths = [0] * max
    for i in range(1, 1000000):
        chain = fact_chain(i)
        if len(chain) == 60:
            count += 1
    print(count)


main()