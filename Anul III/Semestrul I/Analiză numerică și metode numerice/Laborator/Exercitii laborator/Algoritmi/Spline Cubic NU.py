import matplotlib.pyplot as plt
import numpy as np


# dS(a) = df(a) and dS(b) = df(b)
def SplineCubic1(f, df, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    Y = f(X)
    A = Y
    h = np.diff(X)

    AA = np.zeros((n + 1, n + 1))
    AA[0, 0], AA[n, n] = 2*h[0], 2*h[n-1]
    for i in range(1, n):
        AA[i, i] = 2 * (h[i - 1] + h[i])
        AA[i - 1, i] = h[i - 1]
        AA[i, i - 1] = h[i - 1]
    AA[n, n-1], AA[n-1, n] = h[n-1], h[n-1]

    bb = np.zeros(n + 1)
    bb[0] = (3 / h[0]) * (A[1] - A[0]) - 3 * df(X[0])
    bb[n] = 3 * df(X[n]) - (3 / h[n - 1]) * (A[n] - A[n - 1])
    for i in range(1, n):
        bb[i] = (3 / h[i]) * (A[i + 1] - A[i]) - (3 / h[i - 1]) * (A[i] - A[i - 1])

    C = np.linalg.solve(AA, bb)
    B = np.zeros(n)
    B[0] = df(a)
    for i in range(1, n):
        B[i] = (1 / h[i]) * (A[i + 1] - A[i]) - (h[i] / 3) * (2 * C[i] + C[i - 1])

    D = np.zeros(n)
    D[n - 1] = (df(b) - B[n - 1] - 2 * C[n - 1] * h[n - 1]) / (3 * h[n - 1] ** 2)
    for i in range(1, n):
        D[i] = (C[i] - C[i - 1]) / (3 * h[i])

    for i in range(n):
        if X[i] <= x <= X[i + 1]:
            j = i
            break

    return A[j] + B[j] * (x - X[j]) + C[j] * (x - X[j]) ** 2 + D[j] * (x - X[j]) ** 3


def f(x):
    return np.e ** (2 * x)


def df(x):
    return 2 * np.e ** (2 * x)


a = -1
b = 1
n = 5

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

l1 = []
for i in x_graf:
    x = SplineCubic1(f, df, a, b, n, i)
    l1.append(x)

plt.plot(x_graf, y_graf)
plt.plot(x_graf, l1)
plt.show()