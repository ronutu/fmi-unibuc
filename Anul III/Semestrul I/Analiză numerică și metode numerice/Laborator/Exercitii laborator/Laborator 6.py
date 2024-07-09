import numpy as np
import matplotlib.pyplot as plt

def Neville(f, a, b, n, x):
    h = (b - a)/n
    X = []
    Q = np.zeros((n+1, n+1))
    for i in range(n+1):
        X.append(a + i*h)
        Q[i][0] = f(X[i])
        plt.scatter(X[i], f(X[i]))
    for i in range(1, n+1):
        for j in range(1, i+1):
            Q[i, j] = ( Q[i, j - 1]*(x - X[i - j]) - Q[i - 1, j - 1]*(x - X[i]) ) / (X[i] - X[i -j])
    P = Q[n][n]
    return P

f = lambda x: np.e**(2*x)
n = 2
xgraf = np.linspace(-1, 1)
l = []
for x in xgraf:
    l.append(Neville(f, -1, 1, n, x))
    print(Neville(f, -1, 1, n, x))

# plt.plot(x_graf, l)
# plt.plot(x_graf, np.zeros(len(x_graf)))
# plt.show()

plt.plot(xgraf, f(xgraf))
plt.plot(xgraf, l)
plt.show()


errAbs = abs(f(xgraf) - l)
plt.plot(xgraf, errAbs)
plt.plot(xgraf, np.zeros(len(xgraf)))
plt.show()

