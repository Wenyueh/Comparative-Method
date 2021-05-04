import numpy as np
from scipy.io import mmread


def rand_tridiagonal(size):

    diagonal = np.random.rand(size)
    diagonalAbove = np.random.rand(size - 1)
    diagonalBelow = np.random.rand(size - 1)

    matrix = np.zeros((size, size))

    for k in range(size - 1):
        matrix[k][k] = diagonal[k]
        matrix[k][k + 1] = diagonalAbove[k]
        matrix[k + 1][k] = diagonalBelow[k]

    matrix[size - 1][size - 1] = diagonal[size - 1]

    return matrix


def nos_tridiagonal(size):
    # NOS4 matrix, 100*100, block tridiagonal matrix
    # NOS1 matrix, 237 x 237
    # NOS6 matrix, 675*675
    # NOS2 matrix, 957*957
    if size == 100:
        matrix = mmread("nos4.mtx").toarray()
    if size == 250:
        matrix = mmread("nos1.mtx").toarray()
    if size == 500:
        matrix = mmread("nos6.mtx").toarray()
    if size == 1000:
        matrix = mmread("nos2.mtx").toarray()

    return matrix
