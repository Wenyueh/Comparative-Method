import argparse

import matplotlib.pyplot as plt
import numpy as np

from generate_matrix import (band_diagonal, diagonal, diagonal_dominant,
                             rand_tridiagonal, symmetric_definite,
                             symmetric_indefinite)

# Input:
# x: initial guess to the solution
# A: A, diagonal dominant
# b: right-hand side vector
# convergence criterion, here I'm just setting the number of iterations, but we can definitely set a error bound


def Jacobi(num_iterations, A, b, x):
    dists = []
    k = 0
    n = A.shape[0]
    xnew = x.copy()
    while k < num_iterations:
        for i in range(n):
            a = 0
            for j in range(n):
                if i != j:
                    a = a - A[i, j] * x[j]
            xnew[i] = (1 / A[i, i]) * (b[i] + a)
        k += 1
        dist = np.linalg.norm(x - xnew)
        dists.append(dist)
        x = xnew.copy()
        xnew = x.copy()

    y_axis = dists
    x_axis = list(range(num_iterations))

    return xnew, x_axis, y_axis


def GS(num_iterations, A, b, x):
    dists = []
    k = 0
    n = A.shape[0]
    xnew = x.copy()
    while k < num_iterations:
        for i in range(n):
            s1 = np.dot(A[i, :i], xnew[:i])
            s2 = np.dot(A[i, i + 1 :], xnew[i + 1 :])
            xnew[i] = (1 / A[i, i]) * (b[i] - s1 - s2)
        k += 1
        dist = np.linalg.norm(x - xnew)
        dists.append(dist)
        x = xnew.copy()
        xnew = x.copy()

    y_axis = dists
    x_axis = list(range(num_iterations))

    return xnew, x_axis, y_axis


# w: relaxation parameter
def SOR(num_iterations, A, b, x, w):
    dists = []
    k = 0
    n = A.shape[0]
    xnew = x.copy()
    while k < num_iterations:
        for i in range(n):
            s1 = np.dot(A[i, :i], xnew[:i])
            s2 = np.dot(A[i, i + 1 :], xnew[i + 1 :])
            xnew[i] = (1 - w) * x[i] + w * (1 / A[i, i]) * (b[i] - s1 - s2)
        k += 1
        dist = np.linalg.norm(x - xnew)
        dists.append(dist)
        x = xnew.copy()
        xnew = x.copy()

    y_axis = dists
    x_axis = list(range(num_iterations))

    return xnew, x_axis, y_axis


def plot_three_methods(args, num_iterations, A, b, x, w):
    jxnew, jx_axis, jy_axis = Jacobi(num_iterations, A, b, x)
    gxnew, gx_axis, gy_axis = GS(num_iterations, A, b, x)
    sxnew, sx_axis, sy_axis = SOR(num_iterations, A, b, x, w)

    plt.yscale("log") # this is optional
    plt.plot(jx_axis, jy_axis, "b-", gx_axis, gy_axis, "r-", sx_axis, sy_axis, "g-")
    plt.savefig("{}_{}.png".format(args.mtype, args.size), dpi=300)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mtype", type=str, default="diagonal_dominant")
    parser.add_argument("--size", type=int, default=100)
    parser.add_argument("--w", type=float, default=0.9)
    parser.add_argument("--num_iterations", type=int, default=10)
    args = parser.parse_args()

    if args.mtype == "random":
        A = np.random.randint(1, 10, size=(args.size, args.size))
    if args.mtype == "band_diagonal":
        A = band_diagonal(args.size)
    if args.mtype == "diagonal":
        # A = rand_tridiagonal(args.size)
        A = diagonal(args.size)
    if args.mtype == "symmetric_definite":
        A = symmetric_definite(args.size)
    if args.mtype == "symmetric_indefinite":
        A = symmetric_indefinite(args.size)
    if args.mtype == "diagonal_dominant":
        A = diagonal_dominant(args.size)

    b = np.random.randint(-10, 10, size=(A.shape[0], 1))
    x = np.random.rand(A.shape[0], 1)

    plot_three_methods(args, args.num_iterations, A, b, x, args.w)

