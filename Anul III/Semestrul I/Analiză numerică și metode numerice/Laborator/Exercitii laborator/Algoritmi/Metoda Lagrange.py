import matplotlib.pyplot as plt
import numpy as np


def MetLagrange(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    L = np.ones(n+1)
    for i in range(n + 1):
        for j in range(n+1):
            if j != i:
                L[i] *= (x - X[j])/(X[i] - X[j])
    y = 0
    for i in range(n+1):
        y += L[i]*f(X[i])

    return y


def f(x):
    return np.e**(2*x)


a = -1
b = 1
n = 4

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

l = []
for i in x_graf:
    l.append(MetLagrange(f, a, b, n, i))

plt.plot(x_graf, y_graf)
plt.plot(x_graf, l)
plt.show()
