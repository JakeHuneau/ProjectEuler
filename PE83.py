import networkx

matrix = [list(map(int, s.split(','))) for s in open("p082_matrix.txt").readlines()]
row_len, col_len = len(matrix), len(matrix[0])

G = networkx.DiGraph()
for i in range(row_len):
    for j in range(col_len):
        neighbors = [(i+x, j+y) for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)] if 0 <= i+x < row_len and
                     0 <= j+y < col_len]
        for ix, jy in neighbors:
            G.add_edge((i, j), (ix, jy), weight=matrix[ix][jy])
path_len = networkx.dijkstra_path_length(G, source=(0, 0), target=(row_len-1, col_len-1))
print(path_len + matrix[0][0])
