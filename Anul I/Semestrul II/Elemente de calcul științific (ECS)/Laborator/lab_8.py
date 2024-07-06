import numpy as np

# Ex.1:
# a):


def minor(A):
    lista = []
    for k in range(len(A)):
        for i in range(len(A)):
            S = np.copy(A)
            S = np.delete(S, np.s_[i], 0)
            S = np.delete(S, np.s_[k], 1)
            if np.linalg.det(S) > 0:
                lista.append(np.linalg.det(S))
    if len(lista) != len(A)**2:
        return False
    return True


def Cholesky(A):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    assert minor(A), "Matricea A nu are toti minorii principali mai mari decat 0!"
    assert np.all(A == A.T), "Matricea A nu este egala cu transpusa sa!"
    S = np.copy(A)
    L = np.zeros((len(S), len(S)))*float("0")
    for k in range(len(S)):
        L[k, k] = S[k, k]**(1/2)
        for i in range(k+1, len(S)):
            L[i, k] = S[i, k]/L[k, k]
        for i in range(k+1, len(S)):
            for j in range(k+1, len(S)):
                S[i, j] -= L[i, k]*L[j, k]
    return L


# b):
A1 = np.array([[25, 15, -5], [15, 18, 0], [-5, 0, 11]]).astype(float)
A2 = np.array([[25, 16, -5, 1], [15, 18, 0, 2], [-5, 0, 11, 3]]).astype(float)
A3 = np.array([[25, 16, -5], [15, 18, 0], [-5, 0, 11]]).astype(float)
A4 = np.array([[25, 15, -5], [15, 8, 0], [-5, 0, 11]]).astype(float)
# print(Cholesky(A1))
# print(Cholesky(A2))
# print(Cholesky(A3))
# print(Cholesky(A4))

# c):
det = 1
L = Cholesky(A1)
for k in range(len(A1)):
    det *= L[k, k]
det = det**2
# print(det)

# d):
b = np.array([[4], [-3], [-16]]).astype(float)


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


y = sub_asc(L, b)
x = sub_desc(L.T, y)
# print(x)

# Ex. 2:
# a):


def LDL(A):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    assert np.all(A == A.T), "Matricea A nu este egala cu transpusa sa!"
    S = np.copy(A)
    l = Cholesky(A)
    D = np.diag(np.diag(l)**2)
    D1 = np.copy(D)
    for k in range(len(D1)):
        D1[k, k] = D1[k, k]**(-1/2)
    L = l@D1
    return L@D@L.T


# b):
with np.printoptions(precision=14, suppress=True):
    print(LDL(A1))
# print(LDL(A2))
# print(LDL(A3))
# print(LDL(A4))

# c): #TODO

# Ex.3: #TODO

# Ex.4: #TODO
