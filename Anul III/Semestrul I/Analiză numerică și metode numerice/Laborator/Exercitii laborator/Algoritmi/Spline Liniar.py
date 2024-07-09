import matplotlib.pyplot as plt
import numpy as np


def SplineLiniar(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    A = Y[:n]
    B = np.diff(Y)/np.diff(X)
    j = 0
    for i in range(len(X)-1):
        if X[i] <= x <= X[i+1]:
            j = i
            break

    return A[j] + B[j]*(x - X[j])


def f(x):
    return np.e**(2*x)


a = -1
b = 1
n = 5

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

l1 = []
for elem in x_graf:
    l1.append(SplineLiniar(f, a, b, n, elem))

plt.plot(x_graf, y_graf)
plt.plot(x_graf, l1)
plt.show()
