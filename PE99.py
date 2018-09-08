from math import log10

pairs = [list(map(int, s.split(','))) for s in open('p099_base_exp.txt').readlines()]

big = pairs[0][1] * log10(pairs[0][0])  # log a^b = b * log a
indx = 0

for i, pair in enumerate(pairs):
    if pair[1] * log10(pair[0]) > big:
        big = pair[1] * log10(pair[0])
        indx = i

print(indx + 1)