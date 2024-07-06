import numpy as np

# Ex. 1:
# a):


def minor(A):
    lista = []
    for k in range(len(A)):
        for i in range(len(A)):
            S = np.copy(A)
            S = np.delete(S, np.s_[i], 0)
            S = np.delete(S, np.s_[k], 1)
            if np.linalg.det(S) != 0:
                lista.append(np.linalg.det(S))
    if len(lista) != len(A)**2:
        return False
    return True


def LU_fara_pivotare(A):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    assert minor(A), "Matricea nu are toti minorii principali diferiti de 0!"
    L = np.zeros((len(A), len(A))) * float("0")
    U = np.zeros((len(A), len(A))) * float("0")
    S = np.copy(A)
    for k in range(0, len(S)):
        L[k, k] = 1
        U[k, k] = S[k, k]
        for i in range(k+1, len(S)):
            L[i, k] = S[i, k]/U[k, k]
            U[k, i] = S[k, i]
        for i in range(k+1, len(S)):
            for j in range(k+1, len(S)):
                S[i, j] -= L[i, k]*U[k, j]
    return L, U


"""
# b):
A = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
print(LU_fara_pivotare(A))

# c):
det = 1
U = LU_fara_pivotare(A)[1]
for k in range(0, len(A)):
    det *= U[k, k]
print(det)

# d):
"""


def inferior_triunghiulara(L):
    for j in range(1, len(L)):
        for i in range(0, j):
            if L[i, j] != 0:
                return False
    return True


def sub_asc(L, b):
    assert len(L[0]) == len(L), "Matricea L nu este patratica!"
    assert inferior_triunghiulara(L), "Matricea L nu este inferior triunghiulara!"
    assert len(L) == len(b), "Matricea L si vectorul b nu sunt compatibili!"
    assert np.linalg.det(L) != 0, "Matricea L nu este inversabila!"
    x = np.ones((len(L), 1)) * float("nan")
    x[0] = b[0]/L[0, 0]
    for k in range(1, len(L)):
        suma = 0
        for j in range(0, k):
            suma += L[k, j]*x[j]
        x[k] = (b[k]-suma)/L[k, k]
    return x


def superior_triunghiulara(U):
    for i in range(1, len(U)):
        for j in range(0, i):
            if U[i, j] != 0:
                return False
    return True


def sub_desc(U, b):
    assert len(U[0]) == len(U), "Matricea U nu este patratica!"
    assert superior_triunghiulara(U), "Matricea U nu este superior triunghiulara!"
    assert len(U) == len(b), "Matricea U si vectorul b nu sunt compatibili!"
    assert np.linalg.det(U) != 0, "Matricea U nu este inversabila!"
    n = np.shape(U)[0]
    x = np.ones((n, 1))*float("nan")
    x[n-1] = b[n-1]/U[n-1, n-1]
    for k in range(n-2, -1, -1):
         suma = 0
         for j in range(k+1, n):
             suma += U[k, j]*x[j]
         x[k] = (b[k]-suma)/U[k, k]
    return x


def Gauss_Jordan(A):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    I = np.identity(len(A))
    A1 = np.ones((len(A), len(A)))
    for k in range(0, len(A)):
        for i in range(k + 1, len(A)):
            m = A[i, k] / A[k, k]
            for j in range(k + 1, len(A)):
                A[i, j] -= m * A[k, j]
            for z in range(0, len(A)):
                I[i, z] -= m * I[k, z]
            A[i, k] = 0
    for k in range(0, len(A)):
        A1[:, k] = sub_desc(A, I[:, k])[:, 0]
    return A1


"""
b = np.array([[8], [7], [-14], [7]])
L = LU_fara_pivotare(A)[0]
U = LU_fara_pivotare(A)[1]
y = Gauss_Jordan(L)@b
x = Gauss_Jordan(U)@y
print(x)
"""

# Ex.2:
# a):


def LDU(A):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    L = LU_fara_pivotare(A)[0]
    U = LU_fara_pivotare(A)[1]
    D = np.identity(len(A))
    D_1 = np.copy(D)
    diag = []
    for k in range(len(A)):
        diag.append(U[k, k])
    for j in range(len(A)):
        D[j, j] = diag[j]
    diag[:] = [x**(-1) for x in diag]
    for i in range(len(A)):
        D_1[i, i] = diag[i]
    U = D_1@U
    return L, D, U


"""
# b):
A = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
print(LDU(A))

# c):
det = 1
D = LDU(A)[1]
for k in range(0, len(A)):
    det *= D[k, k]
print(det)
"""

# Ex. 3:
# a):


def PLU(A):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    for k in range(len(A)):
        lista = []
        for i in range(k, len(A)):
            lista.append(abs(A[i, k]))
        l = lista.index(max(lista))
        l += k
        P = np.identity(len(A))
        P[[k, l]] = P[[l, k]]
        A = P@A
    L = np.zeros((len(A), len(A))) * float("0")
    U = np.zeros((len(A), len(A))) * float("0")
    L1 = np.zeros((len(A)-1, 1)) * float("0")
    U1 = np.zeros((1, len(A)-1)) * float("0")
    L[0, 0] = 1
    U[0, 0] = A[0, 0]
    for k in range(1, len(A)):
        U1[0, k-1] = A[0, k]
        L1[k-1, 0] = A[k, 0]/U[0, 0]
    S = np.identity(len(A)-1)
    for k in range(0, len(A)-1):
        for i in range(0, len(A)-1):
            S[i, k] = A[i+1, k+1]
    S = S - L1@U1
    print(S)


# b):
A = np.array([[1, 1, -1, 2], [0, 0, -1, 1], [-1, -1, 2, 0], [1, 2, 0, 2]]).astype(float)
print(PLU(A))
