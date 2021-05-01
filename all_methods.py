import numpy as np

# Input:
# x: initial guess to the solution
# A: A, diagonal dominant
# b: right-hand side vector
# convergence criterion, here I'm just setting the number of iterations, but we can definitely set a error bound

num_iterations = 1000


def Jacobi(num_iterations, A, b, x):
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
        improvement = abs(xnew - x)
        print(improvement)
        x = xnew.copy()
        xnew = x.copy()

    return xnew


def GS(num_iterations, A, b, x):
    k = 0
    n = A.shape[0]
    xnew = x.copy()
    while k < num_iterations:
        for i in range(n):
            s1 = np.dot(A[i, :i], xnew[:i])
            s2 = np.dot(A[i, i + 1 :], xnew[i + 1 :])
            xnew[i] = (1 / A[i, i]) * (b[i] - s1 - s2)
        k += 1
        improvement = abs(xnew - x)
        print(improvement)
        x = xnew.copy()
        xnew = x.copy()

    return xnew


# w: relaxation parameter
def SOR(num_iterations, A, b, x, w):
    k = 0
    n = A.shape[0]
    xnew = x.copy()
    while k < num_iterations:
        for i in range(n):
            for i in range(n):
            s1 = np.dot(A[i, :i], xnew[:i])
            s2 = np.dot(A[i, i + 1 :], xnew[i + 1 :])
            xnew[i] = (1 - w) * x[i] + w * (1 / A[i, i]) * (b[i] - s1 - s2)
        k += 1
        improvement = abs(xnew - x)
        print(improvement)
        x = xnew.copy()
        xnew = x.copy()

    return xnew


if __name__ == "__main__":
    A = np.array([[10, -3, 2, 0], [-1, 11, -1, 3], [2, -1.5, 13, -1], [0, 3, -1, 8]])
    b = np.array([6, 25, -11, 10])
    x = np.random.rand(4, 1)
    w = 1

    num_iterations = 10

    output = SOR(num_iterations, A, b, x, w)

    print(output)
