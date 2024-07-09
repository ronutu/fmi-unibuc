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


def Dreptunghi(f, a, b):
    return f((a+b)/2)*(b-a)


def Trapez(f, a, b):
    return ((f(a)+f(b))*(b-a))/2


def Simpson(f, a, b):
    return (f(a)+4*f((a+b)/2)+f(b))/6


def Newton(f, a, b):
    return (f(a)+3*f((2*a+b)/3)+3*f((a+2*b)/3)+f(b))/8


def f(x):
    return np.e**(-x**2)


a = 0
b = 1

dreptunghi = Dreptunghi(f, a, b)
trapez = Trapez(f, a, b)
simpson = Simpson(f, a, b)
newton = Newton(f, a, b)

x = np.linspace(a, b)

# Dreptunghi
plt.subplot(2, 2, 1)
plt.plot(x, f(x))
plt.plot(x, np.linspace(dreptunghi, dreptunghi))

# Trapez
plt.subplot(2, 2, 2)
plt.plot(x, f(x))
plt.plot([a, f(a)], [b, f(b)])
plt.show()

# Simpson
plt.subplot(2, 2, 3)
y_Lagrange = []
for i in x:
    y_Lagrange.append(MetLagrange(f, a, b, 2, i))

plt.plot(x, f(x))
plt.plot(x, y_Lagrange)
plt.show()
