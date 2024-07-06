import numpy as np

# Ex. 1:


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


def max_of_matrix(A):
    lista = []
    for k in range(0, len(A)):
        for i in range(0, len(A)):
            lista.append(A[k, i])
    lista[:] = [abs(x) for x in lista]
    for k in range(0, len(A)):
        for i in range(0, len(A)):
            if abs(A[k, i]) == max(lista):
                return k, i


def MEGPT(A, b):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert len(A) == len(b), "Matricea A si vectorul b nu sunt compatibili!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    for k in range(0, len(A)-1):
        l = max_of_matrix(A)[0]
        m = max_of_matrix(A)[1]
        P = np.identity(len(A))
        Q = np.identity(len(A))
        P[[k, l]] = P[[l, k]]
        Q[:, [k, m]] = Q[:, [m, k]]
        A = P@A@Q
        b = P@b
        for i in range(k + 1, len(A)):
            m = A[i, k] / A[k, k]
            b[i] -= m * b[k]
            for j in range(k + 1, len(A)):
                A[i, j] -= m * A[k, j]
            A[i, k] = 0
    return A, b


"""
# a):
A = np.array([[3, 5, 3], [2, 2, 3], [-1, -3, 0]]).astype(float)
b = np.array([[1], [3], [2]]).astype(float)
print("Ex.1 a):\n" + str(sub_desc(MEGPT(A, b)[0], MEGPT(A, b)[1])))

# b):
for k in range(1, 11):
    eps = 10 ** (-2 * k)
    A = np.array([[eps, 1], [1, 1]]).astype(float)
    b = np.array([[1 + eps], [2]]).astype(float)
    print("Ex.1 b):\n" + str(sub_desc(MEGPT(A, b)[0], MEGPT(A, b)[1])))

# c):
A = np.array([[10 ** (-12), 1, -1], [40, -60, 0], [3, -4, 5]]).astype(float)
b = np.array([[17 + 10 ** (-12)], [-1160], [-62]]).astype(float)
print("Ex.1 c):\n" + str(sub_desc(MEGPT(A, b)[0], MEGPT(A, b)[1])))

# d):
A = np.array([[1, 2, 1], [2, 2, 3], [-1, -3, 1]]).astype(float)
b = np.array([[0], [3], [3]]).astype(float)
print("Ex.1 d):\n"+str(sub_desc(MEGPT(A, b)[0], MEGPT(A, b)[1])))

# e):
for k in range(1, 11):
    C = 10**(2*k)
    A = np.array([[2, 2*C], [1, 1]]).astype(float)
    b = np.array([[2*C], [2]]).astype(float)
    print("Ex.1 e):\n"+str(sub_desc(MEGPT(A, b)[0], MEGPT(A, b)[1])))
"""

# Ex.2:


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
