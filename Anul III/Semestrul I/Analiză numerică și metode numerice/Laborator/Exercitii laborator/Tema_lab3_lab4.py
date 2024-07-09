import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


# Lab 3 - Ex. 2
# (a)
# def f(x):
#     return np.cos(x) - x
#
#
# def Secantaf(f, x0, x1, TOL):
#     aprox_list1 = []
#     while abs(f(x1)) > TOL:
#         x1, x0 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0))), x1
#         aprox_list1.append(x1)
#     return x1, aprox_list1
#
#
# def PozitieFalsaf(f, x0, x1, TOL):
#     aprox_list2 = []
#     x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
#     while abs(f(x2)) > TOL:
#         if f(x2) * f(x1) <= 0:
#             x2, x1, x0 = x2 - f(x2) * ((x2 - x1) / (f(x2) - f(x1))), x2, x1
#         else:
#             x2, x1, x0 = x2 - f(x2) * ((x2 - x0) / (f(x2) - f(x0))), x0, x2
#         aprox_list2.append(x2)
#     return x2, aprox_list2
#
#
# # (b)
# xx1 = Secantaf(f, 0, math.pi/2, 10**-8)[0]
# xx2 = Secantaf(f, math.pi/2, 0, 10**-8)[0]
# xx3 = PozitieFalsaf(f, 0, math.pi/2, 10**-8)[0]
# xx4 = PozitieFalsaf(f, math.pi/2, 0, 10**-8)[0]
# print(xx1, f(xx1))
# print(xx2, f(xx2))
# print(xx3, f(xx3))
# print(xx4, f(xx4))
#
# l1 = Secantaf(f, 0, math.pi/2, 10**-8)[1]
# l2 = PozitieFalsaf(f, math.pi/2, 0, 10**-8)[1]
# graf = np.linspace(0, math.pi/2)
# plt.plot(graf, f(graf), c="green")
# plt.plot(graf, np.zeros(len(graf)), c="black")
# plt.scatter(l1, f(l1), c="red")
# plt.scatter(l2, f(l2), c="purple")
# plt.show()


# Lab 3 - Ex. 2
# (a)
# def f(x):
#     return x**3 - 4*x**2 + 5*x - 2
#
#
# def f_deriv(x):
#     return 3*x**2 - 8*x + 5
#
#
# def phi(x):
#     return x - f(x)/f_deriv(x)
#
#
# def Aitken(f, phi, x0, ITMAX, TOL):
#     iter = 0
#     x1 = phi(x0)
#     x2 = phi(x1)
#     x_caciula = (x2*x0 - x1**2)/(x2 - 2*x1 + x0)
#     l1_iter = []
#     l1_sol = []
#     l1_err_abs = []
#     l1_err_rel = []
#     while abs(f(x_caciula)) >= TOL:
#         iter += 1
#         l1_iter.append(iter)
#         a = x_caciula
#         x_caciula = (x2*x0 - x1**2)/(x2 - 2*x1 + x0)
#         err_abs = abs(a - x_caciula)
#         err_rel = err_abs/abs(a)
#         l1_err_abs.append(err_abs)
#         l1_err_rel.append(err_rel)
#         x2, x1, x0 = phi(x2), x2, x1
#         l1_sol.append(x_caciula)
#         #print("La iteratia {:d}, valoarea lui x este {:.6f}".format(iter, x_caciula))
#         if iter == ITMAX:
#             return x_caciula, l1_iter, l1_sol, l1_err_abs, l1_err_rel
#     return x_caciula, l1_iter, l1_sol, l1_err_abs, l1_err_rel
#
#
# # (b)
# def Steffensen(f, phi, x0, ITMAX, TOL):
#     iter = 0
#     x1 = phi(x0)
#     x2 = phi(x1)
#     x0_caciula = (x2*x0 - x1**2)/(x2 - 2*x1 + x0)
#     x1_caciula = phi(x0_caciula)
#     x2_caciula = phi(x1_caciula)
#     l2_iter = []
#     l2_sol = []
#     l2_err_abs = []
#     l2_err_rel = []
#     while abs(f(x2_caciula)) >= TOL:
#         iter += 1
#         l2_iter.append(iter)
#         a = x0_caciula
#         x0_caciula = (x2_caciula * x0_caciula - x1_caciula ** 2) / (x2_caciula - 2 * x1_caciula + x0_caciula)
#         x1_caciula = phi(x0_caciula)
#         x2_caciula = phi(x1_caciula)
#         l2_sol.append(x0_caciula)
#         err_abs = abs(a - x0_caciula)
#         err_rel = err_abs / abs(a)
#         l2_err_abs.append(err_abs)
#         l2_err_rel.append(err_rel)
#         #print("La iteratia {:d}, valoarea lui x este {:.6f}".format(iter, x0_caciula))
#         if iter == ITMAX:
#             return x0_caciula
#     return x0_caciula, l2_iter, l2_sol, l2_err_abs, l2_err_rel
#
#
# xx1, l1_iter, l1_sol, l1_err_abs, l1_err_rel = (Aitken(f, phi, 0, 20, 10**-10)[0],
#                                                 Aitken(f, phi, 0, 20, 10**-10)[1],
#                                                 Aitken(f, phi, 0, 20, 10**-10)[2],
#                                                 Aitken(f, phi, 0, 20, 10**-10)[3],
#                                                 Aitken(f, phi, 0, 20, 10**-10)[4])
#
# xx2, l2_iter, l2_sol, l2_err_abs, l2_err_rel = (Steffensen(f, phi, 0, 20, 10**-10)[0],
#                                                 Steffensen(f, phi, 0, 20, 10**-10)[1],
#                                                 Steffensen(f, phi, 0, 20, 10**-10)[2],
#                                                 Steffensen(f, phi, 0, 20, 10**-10)[3],
#                                                 Steffensen(f, phi, 0, 20, 10**-10)[4])
#
#
# t1 = [l1_iter, l1_sol, l1_err_abs, l1_err_rel]
# t2 = [l2_iter, l2_sol, l2_err_abs, l2_err_rel]
#
# df1 = {"Iteratia": l1_iter, "Solutia": l1_sol, "Eroarea absoluta": l1_err_abs, "Eroare relativa": l1_err_rel}
# df2 = {"Iteratia": l2_iter, "Solutia": l2_sol, "Eroarea absoluta": l2_err_abs, "Eroare relativa": l2_err_rel}
#
# df1 = (pd.DataFrame(df1)).to_string(index=False)
# df2 = (pd.DataFrame(df2)).to_string(index=False)
#
# print(df1, "\n")
# print(df2)
