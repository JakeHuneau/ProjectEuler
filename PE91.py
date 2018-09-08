from math import gcd

size = 50
result = size * size * 3
for i in range(1, size + 1):
    for j in range(1, size + 1):
        fact = gcd(i, j)
        result += min(j * fact // i, (size - i)*fact // j) * 2

print(result)