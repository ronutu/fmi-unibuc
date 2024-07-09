import matplotlib.pyplot as plt
import numpy as np


def MetNaiva(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    A = np.vander(X)
    C = np.linalg.solve(A, Y)
    C = np.flip(C)
    y = 0
    for i in range(n+1):
        y += C[i] * (x**i)
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
    l.append(MetNaiva(f, a, b, n, i))

plt.plot(x_graf, y_graf, c='b')
plt.plot(x_graf, l)
plt.show()
