import numpy as np

# Ex.1:


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


def MEGFP(A, b):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert len(A) == len(b), "Matricea A si vectorul b nu sunt compatibili!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    assert minor(A), "Matricea A nu are toti minorii principali diferiti de 0!"
    for k in range(0, len(A)):
        for i in range(k+1, len(A)):
            m = A[i, k]/A[k, k]
            b[i] -= m*b[k]
            for j in range(k+1, len(A)):
                A[i, j] -= m*A[k, j]
            A[i, k] = 0
    return A, b


"""
# a):
A = np.array([[3, 5, 3], [2, 2, 3], [-1, -3, 0]]).astype(float)
b = np.array([[1], [3], [2]]).astype(float)
print("Ex.1 a):\n"+str(sub_desc(MEGFP(A, b)[0], MEGFP(A, b)[1])))

# b):
for k in range(1, 11):
    eps = 10**(-2*k)
    A = np.array([[eps, 1], [1, 1]]).astype(float)
    b = np.array([[1+eps], [2]]).astype(float)
    print("Ex.1 b):\n"+str(sub_desc(MEGFP(A, b)[0], MEGFP(A, b)[1])))

# c):
A = np.array([[10**(-12), 1, -1], [40, -60, 0], [3, -4, 5]]).astype(float)
b = np.array([[17+10**(-12)], [-1160], [-62]]).astype(float)
print("Ex.1 c):\n"+str(sub_desc(MEGFP(A, b)[0], MEGFP(A, b)[1])))
"""
# d):
A = np.array([[1, 2, 1], [2, 2, 3], [-1, -3, 1]]).astype(float)
b = np.array([[0], [3], [3]]).astype(float)
print("Ex.1 d):\n"+str(sub_desc(MEGFP(A, b)[0], MEGFP(A, b)[1])))


# Ex.2:


def MEGPP(A, b):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert len(A) == len(b), "Matricea A si vectorul b nu sunt compatibili!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    for k in range(0, len(A)-1):
        lista = []
        for z in range(k, len(A)):
            lista.append(abs(A[z, k]))
        l = lista.index(max(lista))
        l += k
        P = np.identity(len(A))
        P[[k, l]] = P[[l, k]]
        A = P@A
        b = P@b
        for i in range(k + 1, len(A)):
            m = A[i, k]/A[k, k]
            b[i] -= m*b[k]
            for j in range(k+1, len(A)):
                A[i, j] -= m*A[k, j]
            A[i, k] = 0
        print(A)
    return A, b


"""
# a):
A = np.array([[2, 6, 6], [1, 2, 3], [1, 4, 3]]).astype(float)
b = np.array([[14], [6], [8]]).astype(float)
#print(sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1]))

# b):
A = np.array([[2, 6, 6], [1, 2, 3]]).astype(float)
b = np.array([[14], [6]]).astype(float)
#print(sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1]))

# c):
A = np.array([[2, 6, 6], [1, 2, 3], [1, 4, 3]]).astype(float)
b = np.array([[14], [6], [8], [3]]).astype(float)
#print(sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1]))

# d):
A = np.array([[1, 2, 3], [2, 6, 6], [1, 6, 10]]).astype(float)
b = np.array([[6], [14], [17]]).astype(float)
print("Ex.2 d):\n"+str(sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1])))

# e):
for k in range(1, 11):
    eps = 10**(-2*k)
    A = np.array([[eps, 1], [1, 1]]).astype(float)
    b = np.array([[1+eps], [2]]).astype(float)
    print("Ex.2 e):\n"+str(sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1])))

# f):
A = np.array([[10**(-12), 1, -1], [40, -60, 0], [3, -4, 5]]).astype(float)
b = np.array([[17+10**(-12)], [-1160], [-62]]).astype(float)
print("Ex.2 f):\n"+str(sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1])))

# g):
for k in range(1, 11):
    C = 10**(2*k)
    A = np.array([[2, 2*C], [1, 1]]).astype(float)
    b = np.array([[2*C], [2]]).astype(float)
    print("Ex.2 g):\n"+str(sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1])))
"""

# Ex.3:


def max_of_every_row(A):
    lista_finala = []
    for k in range(0, len(A)):
        lista = []
        for i in range(0, len(A)):
            lista.append(A[k, i])
        lista[:] = [abs(x) for x in lista]
        lista_finala.append(max(lista))
    return lista_finala


def MEGPPS(A, b):
    assert len(A[0]) == len(A), "Matricea A nu este patratica!"
    assert len(A) == len(b), "Matricea A si vectorul b nu sunt compatibili!"
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila!"
    S = np.copy(A)
    for k in range(0, len(A)-1):
        s = np.ones((len(A), 1))*float("nan")
        for i in range(k, len(A)):
            s[i] = max_of_every_row(A)[i]
            S[i, k] /= s[i]
        lista = []
        for z in range(k, len(A)):
            lista.append(S[z, k])
        lista[:] = [abs(x) for x in lista]
        l = lista.index(max(lista))
        if k <= l:
            P = np.identity(len(A))
            P[[0, l]] = P[[l, 0]]
            A = P@A
            b = P@b
        for i in range(k + 1, len(A)):
            m = A[i, k]/A[k, k]
            b[i] -= m*b[k]
            for j in range(k+1, len(A)):
                A[i, j] -= m*A[k, j]
            A[i, k] = 0
    return A, b


# Aceleasi subpuncte ca la ex.2
# d):
A = np.array([[1, 2, 3], [2, 6, 6], [1, 6, 10]]).astype(float)
b = np.array([[6], [14], [17]]).astype(float)
print(A@sub_desc(MEGPP(A, b)[0], MEGPP(A, b)[1]))