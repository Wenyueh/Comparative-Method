import numpy as np
from scipy.io import mmread


def check_dominant(name):
    matrix = mmread("{}.mtx".format(name)).toarray()
    abs_matrix = np.abs(matrix)
    n = matrix.shape[0]
    is_dominant = True
    for i in range(n):
        if abs_matrix[i, i] <= sum(abs_matrix[i]) - abs_matrix[i, i]:
            print(i)
            is_dominant = False
    return is_dominant
