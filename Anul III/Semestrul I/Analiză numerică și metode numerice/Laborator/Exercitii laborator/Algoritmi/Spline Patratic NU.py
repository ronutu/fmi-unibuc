import matplotlib.pyplot as plt
import numpy as np


def SplinePatratic(f, df, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    A = Y[:n]
    h = np.diff(X)
    M = np.zeros((2*n, 2*n))
    for i in range(n):
        M[2*i, 2*i] = h[i]
        M[2*i+1, 2*i+1] = 2*h[i]
        M[2*i, 2*i+1] = h[i] ** 2
        if i < n-1:
            M[2*i+1, 2*i+2] = -1
            M[2 * i + 2, 2 * i + 1] = 0
        M[2*i+1, 2*i] = 1

    N_temp = np.diff(Y)
    temp = np.zeros(n)
    N = []
    for i in range(n):
        N.append(N_temp[i])
        N.append(temp[i])
    N[-1] = df(X[-1])

    T = np.linalg.solve(M, N)

    B = []
    C = []
    for i in range(0, len(T), 2):
        B.append(T[i])
        C.append(T[i+1])

    j = 0
    for i in range(len(X)-1):
        if X[i] <= x <= X[i+1]:
            j = i
            break
    return A[j] + B[j]*(x-X[j-1]) + C[j]*((x-X[j-1])**2)


def f(x):
    return np.e**(2*x)


def df(x):
    return 2*np.e**(2*x)


a = -1
b = 1
n = 5

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

l = []
for i in x_graf:
    l.append(SplinePatratic1(f, df, a, b, n, i))

plt.plot(x_graf, y_graf)
plt.plot(x_graf, l)
plt.show()
