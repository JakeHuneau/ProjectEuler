import numpy as np


# Solve by calculating number of paths to each node G[i,j] and solve with G[i,j] = G[i-1,j] + G[i,j-1]

def get_num_paths(row, col):
    row += 1
    col += 1
    num_paths = np.zeros((row, col), dtype=np.uint64)
    num_paths[0, :] = 1
    num_paths[:, 0] = 1
    for r in range(1, row):
        for c in range(1, col):
            num_paths[r, c] = num_paths[r-1, c] + num_paths[r, c-1]
    return num_paths[row-1, col-1]


def main():
    print(get_num_paths(20, 20))


if __name__ == '__main__':
    main()