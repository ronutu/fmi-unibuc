import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


# # Lab 5 - Ex. 2
# # (a)
# def f(x):
#     return np.e**(2*x)
#
#
# def MetLagrange(f, a, b, n, x):
#     X = np.linspace(a, b, n+1)
#     L = np.ones(n+1)
#     for i in range(n+1):
#         for j in range(n+1):
#             if j != i:
#                 L[i] *= (x - X[j])/(X[i] - X[j])
#
#     y = 0
#     for i in range(n+1):
#         y += L[i]*f(X[i])
#     return y
#
#
# n = 2
# a = -1
# b = 1
# x_graf = np.linspace(a, b)
#
# # (b)
# # (b1)
# #
#
# # (b2)
# plt.plot(x_graf, f(x_graf))
# l = []
# for i in x_graf:
#     l.append(MetLagrange(f, a, b, n, i))
# plt.plot(x_graf, l)
# plt.show()
#
# # (b3)
# err_abs = []
# for i in x_graf:
#     err_abs.append(abs(f(i) - MetLagrange(f, a, b, n, i)))
#
# plt.plot(x_graf, err_abs)
# plt.show()

# Lab 6 - Ex. 3
# def f(x):
#     return np.e**(2*x)
#
#
# def DD(x):
#     l = []
#     for k in range(len(x)):
#         suma = 0
#         for i in range(k+1):
#             prod = 1
#             for j in range(k+1):
#                 if i != j:
#                     prod *= (x[i] - x[j])
#             suma += f(x[i])/prod
#         l.append(suma)
#     return l
#
#
# def MetNewtonDD(x, n, l, xx):
#     P = l[0]
#     for i in range(1, n):
#         prod = 1
#         for j in range(0, i):
#             prod *= (x - xx[j])
#         P += l[i] * prod
#     return P
#
#
# # (b)
# # (b1)
#
#
# # (b2)
# a = -1
# b = 1
# n = 2
#
# x_graf = np.linspace(-1, 1)
#
# x_pct = np.linspace(a, b, n+1)
# l = DD(x_pct)
# y_graf = MetNewtonDD(x_graf, n+1, l, x_pct)
#
#
# plt.plot(x_graf, f(x_graf), c='green')
# plt.plot(x_graf, y_graf, c='purple')
# plt.scatter(x_pct, f(x_pct), c='orange')
# plt.show()
#
#
# # (b3)
# err_abs = abs(f(x_graf) - y_graf)
# plt.plot(x_graf, err_abs)
# plt.show()
