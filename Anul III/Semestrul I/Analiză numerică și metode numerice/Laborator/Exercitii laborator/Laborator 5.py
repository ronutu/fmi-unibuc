import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.e**(2*x)

def metNaiv(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    A = np.vander(X) # defineste un def vander-mont
    C = np.linalg.solve(A,Y) # Gauss Pivotat/partiala/faraPivotare/etc ceva de la ecs in loc de linalg.solve (moarte adica)
    C = np.flip(C)
    y = 0
    for i in range(n+1):
        y += C[i] * x**i
        plt.scatter(X,Y)
    # urm 3 linii sunt pt afisarea erorii
    plt.scatter(X, np.zeros(len(X)))
    plt.plot(x, abs(f(x) - y))
    plt.plot(x, np.zeros(len(x)))
    # plt.show()
    return y


def metLagrange(f, a, b, n, x):
    X = np.linspace(a, b, n+1)
    Y = f(X)
    A = np.vander(X) # defineste un def vander-mont
    C = np.linalg.solve(A,Y) # Gauss Pivotat/partiala/faraPivotare/etc ceva de la ecs in loc de linalg.solve (moarte adica)
    C = np.flip(C)
    return

a = -1
b = 1
x_grafic = np.linspace(a,b)
y_grafic = f(x_grafic)

# m = metNaiv(f, -1, 1, 2, x_grafic)
# n = metNaiv(f, -1, 1, 2, x_grafic)

# o = metLagrange(f, -1, 1, 2, x_grafic)


plt.plot(x_grafic, y_grafic)
plt.plot(x_grafic, o)
# plt.plot(x_grafic, n)

plt.show()
