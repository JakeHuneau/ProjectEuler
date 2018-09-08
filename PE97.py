bignum = 1000000000000

n=2
for i in range(7830456):
    n = (2 * n) % bignum

n *= 28433
n += 1

n = n % bignum

print(str(n)[-10:])