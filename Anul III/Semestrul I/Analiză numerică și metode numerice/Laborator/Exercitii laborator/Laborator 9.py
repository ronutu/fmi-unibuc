import matplotlib.pyplot as plt
import numpy as np


# Ex. 1
# a)
def FDM(f, df, x):
    t = int(input("1. Ascendenta\n2. Descendenta\n3. Centrala\n"))

    aprox, err, ordin_conv, h = [], [], [], []
    for k in range(1, 11):
        h.append(10 ** (-k))
        if t == 1:
            f_deriv = (f(x + h[k-1]) - f(x)) / h[k-1]
            aprox.append(f_deriv)
            err.append(abs(df(x) - f_deriv))
            ordin_conv.append(h[k-1])
        elif t == 2:
            f_deriv = (f(x) - f(x - h[k-1])) / h[k-1]
            aprox.append(abs(df(x) - f_deriv))
            err.append(abs(df(x) - f_deriv))
            ordin_conv.append(h[k-1])
        elif t == 3:
            f_deriv = (f(x + h[k-1]) - f(x - h[k-1])) / (2 * h[k-1])
            aprox.append(abs(df(x) - f_deriv))
            err.append(abs(df(x) - f_deriv))
            ordin_conv.append(h[k-1]**2)

    return aprox, err, ordin_conv, h


# b)
def f(x):
    return np.e**(2*x)


def df(x):
    return 2*np.e**(2*x)


x = 0
aprox, err, ordin_conv, h = FDM(f, df, x)
plt.loglog(h, err)
plt.loglog(h, ordin_conv)
plt.show()
