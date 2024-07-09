import matplotlib.pyplot as plt
import numpy as np


def DD(x):
    l = []
    for k in range(len(x)):
        suma = 0
        for i in range(k+1):
            prod = 1
            for j in range(k+1):
                if i != j:
                    prod *= (x[i] - x[j])
            suma += f(x[i])/prod
        l.append(suma)
    return l


def MetNewtonDD(x, n, l, xx):
    P = l[0]
    for i in range(1, n):
        prod = 1
        for j in range(0, i):
            prod *= (x - xx[j])
        P += l[i] * prod
    return P


def f(x):
    return np.e**(2*x)


a = -1
b = 1
n = 4

x_graf = np.linspace(a, b)
y_graf = f(x_graf)

x_pct = np.linspace(a, b, n+1)
l = DD(x_pct)
y = MetNewtonDD(x_graf, n+1, l, x_pct)

plt.plot(x_graf, y_graf)
plt.plot(x_graf, y)
plt.show()

