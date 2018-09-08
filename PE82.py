matrix = [list(map(int, s.split(','))) for s in open('p082_matrix.txt').readlines()]

r, c = len(matrix), len(matrix[0])
tot = [r[-1] for r in matrix]

for i in range(c-2, -1, -1):
    tot[0] += matrix[0][i]
    for j in range(1, r):
        tot[j] = min(tot[j], tot[j-1]) + matrix[j][i]
    for j in range(r-2, -1, -1):
        tot[j] = min(tot[j], tot[j+1] + matrix[j][i])

print(min(tot))