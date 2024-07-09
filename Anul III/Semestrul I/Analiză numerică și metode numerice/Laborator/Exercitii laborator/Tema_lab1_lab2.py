import numpy as np
import matplotlib.pyplot as plt
import math


# Ex. 3 - Lab 1
# def f(x):
#     return x**2 - 3
#
#
# def bis(fct, interval, itmax, tol, opt):
#     a = interval[0]
#     b = interval[1]
#     x = (a + b) / 2
#     i = 0
#
#     if opt == 1:
#         while abs(b - a) >= tol:
#             if fct(a) * fct(x) <= 0:
#                 b = x
#             else:
#                 a = x
#             x = (a + b) / 2
#             i += 1
#             if i == itmax:
#                 print("Numarul maxim de iteratii a fost atins.")
#
#     elif opt == 2:
#         if fct(a) * fct(x) <= 0:
#             b = x
#         else:
#             a = x
#         x_nou = (a + b) / 2
#         while abs(x_nou - x) / abs(x) >= tol:
#             if fct(a) * fct(x_nou) <= 0:
#                 b = x_nou
#             else:
#                 a = x_nou
#             x = x_nou
#             x_nou = (a + b) / 2
#             i += 1
#             if i == itmax:
#                 print("Numarul maxim de iteratii a fost atins.")
#
#     elif opt == 3:
#         while abs(f(x)) >= tol:
#             if fct(a) * fct(x) <= 0:
#                 b = x
#             else:
#                 a = x
#             x = (a + b) / 2
#             i += 1
#             if i == itmax:
#                 print("Numarul maxim de iteratii a fost atins.")
#
#     return x, fct(x)
#
#
# intrvl = [1, 2]
# it = 10**4
# tolr = 10**-8
# print("Alege criteriul de oprire: ")
# print("1. |bn - an| <= TOL\n2. |xn - xn-1| / |xn-1| <= TOL\n3. |f(xn)| <= TOL")
# opti = int(input("Introdu numarul criteriului: "))
#
# print(bis(f, intrvl, it, tolr, opti))


# Ex. 1 - Lab 2
# def f(x):
#     return x**3 + 4*x**2 - 10
#
#
# # (a)
# def MetPunctFix(phi, x, itmax):
#     for i in range(itmax):
#         x = phi(x)
#         print("Aproximarea " + str(i+1) + ": " + str(x))
#     return x


# (b1)
# x1 = np.linspace(1, 2)
# plt.plot(x1, f(x1), color="blue")
# plt.show()


# (b2)
# def phi1(x):
#     return -x**3 - 4*x**2 + x + 10
#
#
# def phi1_deriv(x):
#     return abs(-3*x**2 - 8*x + 1)
#
#
# def phi2(x):
#     return np.sqrt((10/x) - 4*x)
#
#
# def phi2_deriv(x):
#     return abs(-(2*x**2 + 5)/(x**(3/2)*np.sqrt(-4*x**2 + 10)))
#
#
# def phi3(x):
#     return 1/2 * np.sqrt(10 - x**3)
#
#
# def phi3_deriv(x):
#     return abs(-(3*x**2)/(4 * np.sqrt(10 - x**3)))
#
#
# def phi4(x):
#     return np.sqrt(10/(x+4))
#
#
# def phi4_deriv(x):
#     return abs(-(math.sqrt(5))/(math.sqrt(2) * ((x+4) ** (3/2))))


# x1 = np.linspace(1, 2)
# plt.subplot(4, 1, 1)
# plt.plot(x1, phi1(x1), color="blue")
#
# x2 = np.linspace(1, 1.58113883007)
# # aici in loc de intervalul [1,2], am luat intervalul [1, sqrt(5/2)] ca sa nu imi dea eroare
# # in loc de sqrt(5/2) am pus acel nr pt ca in sqrt(5/2) imi da eroare asa ca am luat cu o zecimala mai putin
# plt.subplot(4, 1, 2)
# plt.plot(x2, phi2(x2), color="red")
#
# plt.subplot(4, 1, 3)
# plt.plot(x1, phi3(x1), color="orange")
#
# plt.subplot(4, 1, 4)
# plt.plot(x1, phi4(x1), color="yellow")
# plt.tight_layout()
# plt.show()
#
# plt.subplot(4, 1, 1)
# plt.plot(x1, phi1_deriv(x1), color="blue")
#
# plt.subplot(4, 1, 2)
# plt.plot(x2, phi2_deriv(x2), color="red")
#
# plt.subplot(4, 1, 3)
# plt.plot(x1, phi3_deriv(x1), color="orange")
#
# plt.subplot(4, 1, 4)
# plt.plot(x1, phi4_deriv(x1), color="purple")
# plt.tight_layout()
# plt.show()
#
#
# def g1(x):
#     return phi1(x) - x
#
#
# def g2(x):
#     return phi2(x) - x
#
#
# def g3(x):
#     return phi3(x) - x
#
#
# def g4(x):
#     return phi4(x) - x
#
#
# def brouwer():
#     # nu pot verifica celelalte doua conditii de unicitate asa ca am verificat doar existenta
#     a = 1
#     b = 2
#     if g1(a)*g1(b) < 0:
#         print("phi1 are cel putin un punct fix.")
#         print("Derivata lui phi1 exista.")
#         print("Modul din derivata lui phi1 este mai MARE decat 1 pt orice x din [1, 2].\n")
#     else:
#         print("phi1 nu are niciun punct fix in intervalul dat.")
#
#     if g2(a)*g2(b) < 0:
#         print("phi2 are cel putin un punct fix.")
#     else:
#         print("phi2 nu are niciun punct fix in intervalul dat.\n")
#
#     if g3(a)*g3(b) < 0:
#         print("phi3 are cel putin un punct fix.")
#         print("Derivata lui phi3 exista.")
#         print("Modul din derivata lui phi1 este mai MARE decat 1 pt niste x-uri din [1, 2].\n")
#     else:
#         print("phi3 nu are niciun punct fix in intervalul dat.")
#
#     if g4(a)*g4(b) < 0:
#         print("phi4 are cel putin un punct fix.")
#         print("Derivata lui phi4 exista.")
#         print("Modul din derivata lui phi4 este mai MIC decat 1 pt orice x din [1, 2].\n")
#     else:
#         print("phi4 nu are niciun punct fix in intervalul dat.")
#
#
# brouwer()

# (b3)
# phi4 este singura functie care verifica toate conditiile teoremei lui brouwer
# MetPunctFix(phi4, 1, 20)

# (b4)
# MetPunctFix(phi3, 1, 20)
# print(f(1.3652295783339587))
#
# MetPunctFix(phi4, 1, 20)
# print(f(1.3652300134140969))
# print("phi4 genereaza cel mai rapid.")
