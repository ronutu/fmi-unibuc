# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:07:31 2021

Test Laborator ECS - Paun Liviu-dumitru, Grupa 113

@author: Liviu Paun
"""

#%% EX#1
import numpy as np

# functia mea 6^x
def functie(x):
    return 6**x

# pentru numarator calculez intai derivata, care pt 6^x este ln6 * 6^x, mai apoi ln^2(6) * 6^x...
def derivata(n):
    b = np.log(6)
    return b**n

# pentru numitor calculez factorialul 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# calculez (x-a)^k 
def putere(x, a, n):
    return (x-a)**n

 
x = -2       # calculez sumele partiana in punctul x = -2
serie = 0    # initializez seria
a = -1       # pentru punctul a = -1
epsilon = 1  #eroarea relativa
n = 0
 
while epsilon > 10**(-9):
    serie = (serie + (functie(a) * derivata(n)) / (factorial(n)) * putere(x, a, n))
    eroare_absoluta = abs(functie(x) - serie)
    epsilon = abs(functie(x) - serie) / abs(functie(x))
    print(n, '\t', "%.12f"%serie,'\t', "%.12f"%functie(x), '\t', "%.2e"%eroare_absoluta, '\t', "%.2e"%epsilon)
    n += 1
 
print("N minim pentru ca eroarea relativa a aproximarii obtinute folosind suma partiala sa fie mai mica decat", 10**(-9), "este N =", n-1)

#%% EX#2   a)  verificam daca admite:

"""
Conditii pentru justificare:
    MEGFP:
        i. A este o matrice pătratică
        ii. A este matrice inversabilă
        iii. la fiecare pas, akk ≠ 0
        iv. matricea A și vectorul b sunt compatibili (pentru rezolvare de sisteme)

    LUfp: A admite MEGFP
    
    PLU: matricea A este inversabilă
    
    MEGPP/MEGPPS/MEGPPT:
        i. A este o matrice pătratică
        ii. A este matrice inversabilă
        iii. matricea A și vectorul b sunt compatibili (pentru rezolvare de sisteme)
    Cholesky:
        i. matricea A este pătratică și A=AT
        ii. A este matrice inversabilă
        iii. toți determinanții de colț (minorii, începând cu a11, după care bordăm
    până ajungem la det(A)) al lui A să fie pozitivi
"""

def exc2a(A, b):
    # (0) Verifica daca matricea A este patratica
    n = np.shape(A)[0]
    assert n == np.shape(A)[1], "Matricea nu e patratica"    
   
    # (1) Verifica daca A si b au acelasi numar de linii
    assert n == np.shape(b)[0], "A si b nu au acelasi numar de linii"
    
    # (i) Verifica daca A admite MEGFP
    for k in range(n-1):
        assert abs(np.linalg.det(A[:k+1,:k+1])) >1e-14, "A nu admite MEGFP, si deci nu admite LUfp"
    
    # (ii) Verifica daca A admite LUfp
    assert abs(np.linalg.det(A)) > 1e-14, "A nu admite PLU"
   
    # (iii) Verifica daca A admite MEGFP
    for k in range(n-1):
        assert abs(np.linalg.det(A[:k+1,:k+1])) > 1e-14, "A nu admite MEGFP"
    
    # (iv) Verifica daca A admite MEGPPS #M: E de ajuns sa verificam ca matricea este inversabila pentru MEGPPS
    assert A[0,0] != 0, "Matricea nu admite MEGPPS"
    for k in range(1,n):
        assert abs(np.linalg.det(A[:k+1,:k+1])) > 1e-14,  "Matricea A nu admite MEGPP/MEGPPT/MEGPPS"
    
    # (v) Verifica daca A admite Factorizare Cholesky
    assert A[0,0] > 0, "Matricea A nu admite factorizare Cholesky"
    
    # (vi) Verifica daca A este (strict) diagonal dominanta
    c = 0  #iau o variabila c care numara liniiile pe care termenul de pe diag prin este >= cu restul
    for i in range(n):
        for j in range(n):
            if A[i,i] >= A[i,j]: 
                c += 1
    if c == n*n: 
        print("e diag dominanta")
    else: print("nu e diag dominanta")
    
    return A

A = np.array([
    [8, 0, -5, 9],
    [0, 3, -6, 0],
    [-1, 6, -10, 4],
    [2, 7, -8, 3]
    ]).astype(float)

b = np.array([
    [65],
    [-21],
    [-6],
    [16]
    ]).astype(float)

exc2a(A, b)

#%% EX#2   b)  Determinam solutia sistemului Ax = b cu LUfp

def FactLUfp(A):
    """
    Factorizarea LU fara pivotare (LUfp): Factorizarea matricii A in A = L * U
    fara pivotare, unde L este o matrice inferior triunghiulara cu elementele
    de pe diagonala egale cu 1 si U este o matrice superior triunghiulara.
    :param A (numpy square matrix of floats) = matricea initiala a sistemului;
    :return L (numpy square matrix of floats) = matrice inferior triunghiulara;
    :return U (numpy square matrix of floats) = matrice superior triunghiulara;
    """   
    # (i) Verifica daca matricea A este patratica
    n = np.shape(A)[0]
    assert n == np.shape(A)[1], "Matricea nu e patratica"       
   
    # (ii) Verifica daca A admite LUfp: MEGFP
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    S = np.copy(A)
    for k in range(0,n):
        L[k,k] = 1
        U[k,k] = S[k,k]
        for i in range(k+1,n):  
            L[i,k] = S[i,k] / U[k,k]
            U[k,i] = S[k,i]
        for i in range(k+1,n):
            for j in range(k+1,n):
                S[i,j] = S[i,j] - L[i,k]*U[k,j]
    return L, U

def SubsAsc(L, b):
    """
    Metoda Substitutiei Ascendente: Determina solutia sistemului inferior
    triunghiular L * x = b folosind metoda substitutiei ascendente.
    :param L (numpy square matrix of floats) = matrice inferior triunghiulara;
    :param b (numpy column vector of floats) = coloana termenilor liberi;
    :return x (numpy column vector of floats) = solutia sistemului;
    """
    # (i) Verifica daca matricea L este patratica
    n = np.shape(L)[0]  # Salvam in variabila n dimensiunea matricii
    assert n == np.shape(L)[1], "matricea nu e patratica"
    
    # (ii) Verifica daca matricea L este inferior triunghiulara
    for i in range(n): 
        for j in range(i+1, n):
             assert L[i,j] == 0, "Matricea nu e inferior triunghiulara"
    
    # (iii) Verifica daca L si b au acelasi numar de linii
    assert n == np.shape(b)[0], "L si b nu au acelasi numar de linii"
    
    # (iv) Verifica daca L este inversabila: 
    det = 1
    for i in range(0,n):
        det = det*L[i,i]
    assert det != 0, "L nu este inversabila"
   
    # Initializeaza vectorul x ca vector coloana numpy
    x = float('nan') * np.ones((n, 1))

    # Metoda substitutiei ascendente
       
    x[0] = b[0] / L[0,0]  
    
    for k in range(1,n):
        s = 0
        for p in range(k):
            s += L[k,p] * x[p]
        x[k] = (b[k]-s) / L[k,k]
    return x

def SubsDesc(U, b):
    """
    Metoda Substitutiei Descendente: Determina solutia sistemului superior
    triunghiular U * x = b folosind metoda substitutiei descendente
    :param U (numpy square matrix of floats) = matrice superior triunghiulara;
    :param b (numpy column vector of floats) = coloana termenilor liberi;
    :return x (numpy column vector of floats) = solutia sistemului;
    """
    # (i) Verifica daca matricea U este patratica
    n = np.shape(U)[0]  # Salvam in variabila n dimensiunea matricii
    assert n == np.shape(U)[1], "Matricea nu e patratica"
    
    # (ii) Verifica daca matricea U este superior triunghiulara
    for i in range(n): 
        for j in range(0,i):
             assert U[i,j] == 0, "Matricea nu e superior triunghiulara"
    
    # (iii) Verifica daca U si b au acelasi numar de linii
    assert n == np.shape(b)[0], "U si b nu au acelasi numar de linii"
    
    # (iv) Verifica daca U este inversabila: 
    det = 1
    for i in range(0,n):
        det = det * U[i,i]
    assert det != 0, "U nu este inversabila"
    
    # Initializeaza vectorul x ca vector coloana numpy
    x = float('nan') * np.ones((n, 1))
        
    # Metoda substitutiei descendente
     
    x[n-1] = b[n-1] / U[n-1,n-1]  
    
    for k in range(n-2,-1,-1):
        s = 0
        for p in range(k+1,n):
            s += U[k,p] * x[p]
        x[k] = (b[k]-s) / U[k,k]  
    return x

A = np.array([
    [8, 0, -5, 9],
    [0, 3, -6, 0],
    [-1, 6, -10, 4],
    [2, 7, -8, 3]
    ]).astype(float)

b = np.array([
    [65],
    [-21],
    [-6],
    [16]
    ]).astype(float)

L, U = FactLUfp(A)
y = SubsAsc(L, b)
x = SubsDesc(U, y)
print("Solutia este X= ", x)
