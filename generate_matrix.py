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


def diagonal(size):
    # BCSSTM22 matrix, 138 x 138
    # BCSSTM20 matrix, 485 x 485
    # BCSSTM19 matrix, 817 x 817
    # BCSSTM26 matrix, 1922 x 1922
    if size == 100:
        matrix = mmread("bcsstm22.mtx").toarray()
    if size == 500:
        matrix = mmread("bcsstm20.mtx").toarray()
    if size == 800:
        matrix = mmread("bcsstm19.mtx").toarray()
    if size == 2000:
        matrix = mmread("bcsstm26.mtx").toarray()

    return matrix


def band_diagonal(size):
    # NOS4 matrix, 100*100, block tridiagonal matrix
    # NOS1 matrix, 237 x 237
    # NOS6 matrix, 675 x 675
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


def symmetric_definite(size):
    # BCSSTK01 48 x 48
    # BCSSTK04: 132 x 132
    # BCSSTK08: 1074 x 1074
    if size == 50:
        matrix = mmread("bcsstk01.mtx").toarray()
    if size == 100:
        matrix = mmread("bcsstk04.mtx").toarray()
    if size == 1000:
        matrix = mmread("bcsstk08.mtx").toarray()

    return matrix


def symmetric_indefinite(size):
    # BCSSTK22: 138 x 138
    # bfw398b: 398 x 398
    # BCSSTK19: 817 x 817
    if size == 100:
        matrix = mmread("bcsstk22.mtx").toarray()
    if size == 500:
        matrix = mmread("bfw398b.mtx").toarray()
    if size == 1000:
        matrix = mmread("bcsstk19.mtx").toarray()

    return matrix


def diagonal_dominant(size):
    # bcsstm22: 138 x 138
    # NOS6 matrix, 675 x 675
    if size == 100:
        matrix = mmread("bcsstm22.mtx").toarray()
    if size == 500:
        matrix = mmread("nos6.mtx").toarray()

    return matrix
