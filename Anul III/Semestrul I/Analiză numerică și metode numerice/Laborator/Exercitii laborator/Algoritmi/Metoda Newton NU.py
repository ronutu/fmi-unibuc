import matplotlib.pyplot as plt
import numpy as np


def MetNewton(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    c, P = np.ones(n+1), np.ones(n+1)
    c[0] = Y[0]
    P[0] = c[0]
    for i in range(1, n+1):
        prod1 = 1
        prod2 = 1
        for j in range(i):
            prod1 *= X[i] - X[j]
            prod2 *= x - X[j]
        c[i] = (Y[i] - P[i-1]) / prod1
        P[i] = P[i-1] + c[i]*prod2
    return P[-1]


def f(x):
    return np.e**(2*x)


a = -1
b = 1
n = 4

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

l = []
for i in x_graf:
    l.append(MetNewton(f, a, b, n, i))

plt.plot(x_graf, y_graf)
plt.plot(x_graf, l)
plt.show()
