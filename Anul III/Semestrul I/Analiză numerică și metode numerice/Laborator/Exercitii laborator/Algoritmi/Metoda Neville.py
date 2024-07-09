import matplotlib.pyplot as plt
import numpy as np


def MetNeville(f, a, b, n, x):
    h = (b - a)/n
    X = []
    Q = np.zeros((n+1,n+1))
    for i in range(n+1):
        X.append(a+i*h)
        Q[i, 0] = f(X[i])
    for i in range(1, n+1):
        for j in range(1, i+1):
            Q[i, j] = (Q[i, j-1] * (x - X[i-j]) - Q[i-1, j-1] * (x - X[i])) / (X[i] - X[i-j])

    P = Q[n, n]
    return P


def f(x):
    return np.e**(2*x)


a = -1
b = 1
n = 4

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

l = []
for i in x_graf:
    l.append(MetNeville(f, a, b, n, i))

plt.plot(x_graf, y_graf)
plt.plot(x_graf, l)
plt.show()
