# Davidescu-Filip Olivia-Alexandra
# Anul I, Seria 10, Grupa 103
# 15.04.2021
# Test de Laborator

import numpy as np
from numpy.linalg import det
import math


# Exercitiul 1
def aprox_functie(x, a, TOL, ITMAX):
    l = np.zeros(ITMAX + 1)
    fact = 1
    l[0] = 1
    val_ex = 4 ** x
    i = 0
    err_abs_num = 1
    err_rel_num = 1
    while err_rel_num > TOL and i < ITMAX:
        i = i + 1
        fact = fact * i
        t = ((4 ** a) * (np.log(4) ** i)) / fact * ((x - a) ** i)
        l[i] = l[i - 1] + t
        err_abs = abs(val_ex - l[i])
        err_abs_num = abs(t)
        err_rel = err_abs / abs(val_ex)
        err_rel_num = err_abs_num / abs(l[i])
        print('%2i \t %.12f \t %.12f \t %.2e \t %.2e \t %.2e \t %.2e' % (
        i, val_ex, l[i], err_abs, err_abs_num, err_rel, err_rel_num))
    print("N minim astfel incat eroarea relatva a aproximarii sa fie mai mica decat epsilon este", i)

x = 3
a = -2
TOL = 10 ** (-10)
ITMAX = 1000
rezultat = aprox_functie(x, a, TOL, ITMAX)
print(rezultat)


# Exercitiul 2
A = np.array([[-2, -4, -7, 2], [3, -3, 3, 9], [-7, 7, -7, 1], [0, -7, 6, -8]]).astype('float')
b = np.array([[-23], [42], [-10], [-28]]).astype('float')

# (a)
# (i) Verificam daca matricea asociata sistemului dat admite factorizarea LU fara pivotare
# Matricea trebuie sa fie patratica, inversabila, compatibila cu vectorul si akk != 0 la fiecare pas
# Conditiile sunt aceleasi pentru factorizarea LU fara pivotare si MEGFP
def factorizare_LUFP(A):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Factorizare LU fara Pivotare nu e posibila deoarece matricea sistemului nu este patratica')
        return False
    if np.shape(A)[0] != np.shape(b)[0]:
        print('Factorizare LU fara Pivotare nu e posibila deoarece matricea sistemului si vectorul nu sunt compatibili')
        return False
    if det(A) == 0:
        print('Factorizare LU fara Pivotare nu e posibila deoarece matricea sistemului nu este inversabila')
        return False
    if A[0, 0] == 0:
        print('Factorizare LU fara Pivotare nu e posibila deoarece avem primul element nul pe diagonala principala')
        return False
    n = np.shape(A)[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    U[0, 0] = A[0, 0]
    U[0, 1:n] = A[0, 1:n]
    L[1:n, 0] = A[1:n, 0] / U[0, 0]
    for i in range(1, n):
        U[i, i] = A[i, i] - L[i, 0:i] @ U[0:i, i]
        if U[i, i] == 0:
            print(
                'Factorizare LU fara Pivotare nu e posibila deoarece avem element nul pe diagonala principala la pasul ',
                i + 1)
            return False
        for j in range(i + 1, n):
            U[i, j] = A[i, j] - L[i, 0:i] @ U[0:i, j]
            L[j, i] = (A[j, i] - L[j, 0:i] @ U[0:i, i]) / U[i, i]
    return True

if factorizare_LUFP(A):
    print('Factorizarea LU fara Pivotare e posibila')


# (ii) Verificam daca matricea asociata sistemului dat admite factorizare LU cu pivotare
# Matricea trebuie sa fie patratica si inversabila
def factorizare_PLU(A):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Factorizare LU cu Pivotare nu e posibila deoarece matricea nu este patratica')
        return False
    if det(A) == 0:
        print('Factorizare LU cu Pivotare nu e posibila deoarece matricea sistemului nu este inversabila')
        return False

if factorizare_PLU(A):
    print('Factorizarea LU cu Pivotare Partiala e posibila')


# (iii) Verificam daca matricea asociata sistemului dat admite Metoda Eliminarii Gauss fara Pivotare
# Matricea trebuie sa fie patratica, inversabila, compatibila cu vectorul si akk != 0 la fiecare pas
# Conditiile sunt aceleasi pentru factorizarea LU fara pivotare si MEGFP
def MEGFP(A, b):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Nu putem aplica MEGFP deoarece matricea sistemului nu este patratica')
        return False
    if np.shape(A)[0] != np.shape(b)[0]:
        print('Nu putem aplica MEGFP deoarece matricea sistemului si vectorul nu sunt compatibili')
        return False
    if det(A) == 0:
        print('Nu putem aplica MEGFP deoarece matricea sistemului nu este inversabila')
        return False
    A_ext = np.hstack((A, b))
    n = np.shape(A)[0]
    for k in range(n - 1):
        if A_ext[k, k] == 0:
            print('Nu putem aplica MEGFP deoarece avem element nul pe diagonala principala la pasul ', k + 1)
            return False
    return True

if MEGFP(A, b):
    print('Se poate aplica Metoda Eliminarii Gauss fara Pivotare')


# (iv) Verificam daca matricea asociata sistemului dat admite Metoda Eliminarii Gauss cu Pivotare
# Conditiile sunt aceleasi pentru cele trei metode - cu pivotare partiala, partiala scalata sau totala :
# Matricea trebuie sa fie patratica, inversabila si compatibila cu vectorul

# Verificam daca matricea asociata sistemului dat admite Metoda Eliminarii Gauss cu Pivotare Partiala
def MEGPP(A, b):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Nu putem aplica MEGPP deoarece matricea sistemului nu este patratica')
        return False
    if np.shape(A)[0] != np.shape(b)[0]:
        print('Nu putem aplica MEGPP deoarece matricea sistemului si vectorul nu sunt compatibili')
        return False
    if det(A) == 0:
        print('Nu putem aplica MEGPP deoarece matricea sistemului nu este inversabila')
        return False
    n = np.shape(A)[0]
    A_ext = np.hstack((A, b))
    for k in range(n - 1):
        max_col = abs(A_ext[k:n, k]).max()
        if max_col == 0:
            print('Matricea sistemului nu e inversabila')
            return False
    return True

# Verificam daca matricea asociata sistemului dat admite Metoda Eliminarii Gauss cu Pivotare Partiala Scalata
def MEGPPS(A, b):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Nu putem aplica MEGPPS deoarece matricea sistemului nu este patratica')
        return False
    if np.shape(A)[0] != np.shape(b)[0]:
        print('Nu putem aplica MEGPPS deoarece matricea sistemului si vectorul nu sunt compatibili')
        return False
    if det(A) == 0:
        print('Nu putem aplica MEGPPS deoarece matricea sistemului nu este inversabila')
        return False
    n = np.shape(A)[0]
    A_ext = np.hstack((A, b))
    s = np.zeros(n)
    for k in range(n - 1):
        for l in range(k, n):
            s[l] = abs(A_ext[l, k:n]).max()
            if s[l] == 0:
                print('Matricea sist nu e inv')
                return False
        max_col_rel = abs(A_ext[k:n, k] / s[k:n]).max()
        if max_col_rel == 0:
            print('Matricea sistemului nu e inversabila')
            return False
    return True

# Verificam daca matricea asociata sistemului dat admite Metoda Eliminarii Gauss cu Pivotare Totala
def MEGPT(A, b):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Nu putem aplica MEGPT deoarece matricea sistemului nu este patratica')
        return False
    if np.shape(A)[0] != np.shape(b)[0]:
        print('Nu putem aplica MEGPT deoarece matricea sistemului si vectorul nu sunt compatibili')
        return False
    if det(A) == 0:
        print('Nu putem aplica MEGPT deoarece matricea sistemului nu este inversabila')
        return False
    n = np.shape(A)[0]
    A_ext = np.hstack((A, b))
    indicii_x = np.arange(n)
    for k in range(n - 1):
        # print('k=',k)
        # print(A_ext)
        max_submatrice = abs(A_ext[k:n, k:n]).max()
        if max_submatrice == 0:
            print('Matricea sist nu e inv')
            return False
        # print(max_submatrice)
    return True

if MEGPP(A, b):
    print('Se poate aplica Metoda Eliminarii Gauss cu Pivotare Partiala')
if MEGPPS(A, b):
    print('Se poate aplica Metoda Eliminarii Gauss cu Pivotare Partiala Scalata')
if MEGPT(A, b):
    print('Se poate aplica Metoda Eliminarii Gauss cu Pivotare Totala')


# (v) Verificam daca matricea asociata sistemului dat admite factorizare Cholesky
# Matricea trebuie sa fie patratica, simetrica, inversabila si pozitiv definita
def factorizare_Cholesky(A):
    if np.shape(A)[0] != np.shape(A)[1]:
        print("Factorizare Cholesky nu e posibila deoarece matricea nu e patratica.")
        return False
    if (A != np.transpose(A)).any():
        print('Factorizare Cholesky nu e posibila deoarece matricea nu e simetrica')
        return False
    n = np.shape(A)[0]
    if A[0, 0] <= 0:
        print("Factorizare Cholesky nu e posibila deoarece matricea nu e pos def")
        return False
    if det(A) == 0:
        print('Factorizare Cholesky nu e posibila deoarece matricea sistemului nu este inversabila')
        return False
    L = zeros((n, n))
    L[0, 0] = sqrt(A[0, 0])
    L[1:n, 0] = A[1:n, 0] / L[0, 0]
    for i in range(1, n):
        alpha = A[i, i] - L[i, 0:i] @ L[i, 0:i]
        if alpha <= 0:
            print("Factorizare Cholesky nu e posibila deoarece matricea nu e pos def")
            return False
    return True

if factorizare_Cholesky(A):
    print('Factorizarea Cholesky e posibila')


# (vi) Verificam daca matricea asociata sistemului dat este diagonal dominanta
def Diag_Dom(A):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Nu este diagonal dominanta, deoarece matricea nu este patratica')
        return False
    n = np.shape(A)[0]
    for i in range(n):
        suma = 0
        for j in range(n):
            if i != j:
                suma = suma + abs(A[i, j])
        if abs(A[i, i]) < suma:
            print("Matricea nu este Strict Diagonal Dominanta deoarece suma modulului elementelelor de pe diagonala principala este mai mica sau egala cu suma elementelor de pe linia sa ")
            return False
    return True

if Diag_Dom(A):
    print('Matricea este (strict) Diagonal Dominanta')


# (b) Determinam solutia sistemului folosind Metoda Eliminarii Gauss cu Pivotare Partiala Scalata
def MEGPPS(A, b):
    if np.shape(A)[0] != np.shape(A)[1]:
        print('Nu putem aplica MEGPPS deoarece matricea sistemului nu este patratica')
        return False
    if np.shape(A)[0] != np.shape(b)[0]:
        print('Nu putem aplica MEGPPS deoarece matricea sistemului si vectorul nu sunt compatibili')
        return False
    if det(A) == 0:
        print('Nu putem aplica MEGPPS deoarece matricea sistemului nu este inversabila')
        return False
    n = np.shape(A)[0]
    A_ext = np.hstack((A, b))
    s = np.zeros(n)
    for k in range(n - 1):
        for l in range(k, n):
            s[l] = abs(A_ext[l, k:n]).max()
            if s[l] == 0:
                print('Matricea sist nu e inv')
                return
        max_col_rel = abs(A_ext[k:n, k] / s[k:n]).max()
        if max_col_rel == 0:
            print('Matricea sistemului nu e inversabila')
            return
        p = np.where(abs(A_ext[k:n, k] / s[k:n]) == max_col_rel)
        p_ind = p[0][0]
        p_ind = p_ind + k
        if p_ind > k:
            A_ext[[p_ind, k], :] = A_ext[[k, p_ind], :]
        for l in range(k + 1, n):
            m = A_ext[l, k] / A_ext[k, k]
            A_ext[l, :] = A_ext[l, :] - m * A_ext[k, :]
    Anew = A_ext[0:n, 0:n]
    bnew = A_ext[:, n]
    x = MetSubsDesc(Anew, bnew)
    return x

def cond_sup(L, b):
    if np.shape(L)[0] != np.shape(L)[1]:
        print('Matricea sistemului nu este patratica')
        return False
    for i in range(np.shape(L)[0]):
        for j in range(0, i):
            if L[i, j] != 0:
                print('Matricea sistemului nu este superior triunghiulara')
                return False
    if np.shape(L)[0] != np.shape(b)[0]:
        print('Matricea sistemului si vectorul nu sunt compatibili dpdv al dimensiunii')
        return False
    for i in range(np.shape(L)[0]):
        if L[i, i] == 0:
            print('Matricea sistemului nu este inversabila')
            return False


def MetSubsDesc(A, b):
    if cond_sup(A, b) == False:
        return
    n = len(b)
    x = np.zeros((n, 1))
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for k in range(n - 2, -1, -1, ):
        x[k] = (b[k] - A[k, k + 1:n] @ x[k + 1:n]) / A[k, k]
    return x

rezultat2 = MEGPPS(A, b)
print("Solutia sistemului este ", rezultat2)