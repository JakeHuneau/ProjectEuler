matrix = [list(map(int, j.split(','))) for j in open('p081_matrix.txt').readlines()]

rows, cols = len(matrix), len(matrix[0])

for r in range(rows):
    for c in range(cols):
        matrix[r][c] += min(matrix[r-1][c], matrix[r][c-1]) if r*c > 0 else (matrix[r-1][c] if r else (matrix[r][c-1]
                                                                                                       if c else 0))

print(matrix[-1][-1])