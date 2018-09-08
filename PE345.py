import numpy as np
from collections import defaultdict

matrix_str = """  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303"""


matrix = np.array([list(filter(None, s.split(' '))) for s in matrix_str.split('\n')], dtype=np.int)

def hungarian_algorithm(mat):

    for r_ind, row in enumerate(mat):
        row_max = max(row)
        for c_ind, val in enumerate(row):
            mat[r_ind, c_ind] = row_max - val

    for c_ind, col in enumerate(mat.transpose()):
        col_max = max(col)
        for r_ind, val in enumerate(col):
            mat[r_ind, c_ind] = col_max - val

    print(mat)

hungarian_algorithm(matrix)
