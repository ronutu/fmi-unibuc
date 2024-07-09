import matplotlib.pyplot as plt
import numpy as np


def Richardson(f, x, n):
    h = []
    for k in range(1, 11):
        h.append(10 ** (-k))
    return


def f(x):
    return np.e**(2*x)


def df(x):
    return 2*np.e**(2*x)


x = 0
n = 3
