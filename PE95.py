from Project_Euler import factors

def factor_sum(n):
    return sum(sorted(list(factors(n)))[:-1])

L = 1000000
d = [1] * L  # number of divisors
for i in range(2, L // 2):
    for j in range(2*i, L, i):
        d[j] += i

max_cl = 0
min_link = 0
for i in range(2, L):
    n, chain = i, []
    while d[n] < L:
        d[n], n = L+1, d[n]
        try:
            k = chain.index(n)
        except ValueError:
            chain.append(n)
        else:
            if len(chain[k:]) > max_cl:
                max_cl, min_link = len(chain[k:]), min(chain[k:])

print(min_link)
