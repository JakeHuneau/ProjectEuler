from decimal import getcontext, Decimal


getcontext().prec = 102

tot = 0
for i in range(2, 100):
    d = Decimal(i).sqrt()
    tot += sum(int(j) for j in str(d * 10 ** 99)[:100]) if d % 1 != 0 else 0

print(tot)