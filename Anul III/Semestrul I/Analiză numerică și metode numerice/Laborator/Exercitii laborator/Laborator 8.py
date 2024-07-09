import matplotlib.pyplot as plt
import numpy as np


def SplineLiniar(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    h = np.diff(X)  # h = [x1-x0, x2-x1, ..., xn-xn-1]
    print(Y)
    print(Y[:n])
    A = Y[:n]
    B = np.diff(Y)/h
    for i in range(n):
        if X[i] <= x <= X[i + 1]:
            j = i
            break
    return A[j] + B[j]*(x-X[j])


def f(x):
    return np.e**(2*x)


a = -1
b = 1
n = 5

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

l = []
for i in x_graf:
    l.append(SplineLiniar(f, a, b, n, i))

plt.plot(x_graf, y_graf)
plt.plot(x_graf, l)
plt.show()
