import numpy as np

# Ex.1:
A1 = np.array([[0.10, 0.10], [0.17, 0.11], [2.02, 1.29]]).astype(float)
b1 = np.array([[0.26], [0.28], [3.31]]).astype(float)
A2 = np.array([[0.10, 0.10], [0.17, 0.11], [2.02, 1.29]]).astype(float)
b2 = np.array([[0.27], [0.25], [3.33]]).astype(float)
A3 = np.array([[1, -1], [0, 10**(-10)], [0, 0]]).astype(float)
b3 = np.array([[0], [10**(-10)], [1]]).astype(float)

# a):


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
    #assert minor(A), "Matricea A nu are toti minorii principali diferiti de 0!"
    for k in range(0, len(A)):
        for i in range(k+1, len(A)):
            m = A[i, k]/A[k, k]
            b[i] -= m*b[k]
            for j in range(k+1, len(A)):
                A[i, j] -= m*A[k, j]
            A[i, k] = 0
    return A, b


def PCMMP1(A, b):
    assert len(A) >= len(A[0]), "Numarul de linii este mai mic decat numarul de coloane!"
    S = A.T@A
    assert np.linalg.det(S) != 0, "Matricea S nu este inversabila la stanga!"
    assert len(A) == len(b), "Matricea A nu are acelasi numar de linii cu vectorul b!"
    c = A.T@b
    S = MEGFP(S, c)[0]
    c = MEGFP(S, c)[1]
    return sub_desc(S, c), b-A@sub_desc(S, c)


# b):
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


def PCMMP2(A, b):
    assert len(A) >= len(A[0]), "Numarul de linii este mai mic decat numarul de coloane!"
    S = A.T@A
    assert np.linalg.det(S) != 0, "Matricea S nu este inversabila la stanga!"
    assert len(A) == len(b), "Matricea A nu are acelasi numar de linii cu vectorul b!"
    c = A.T@b
    S = MEGPP(S, c)[0]
    c = MEGPP(S, c)[1]
    return sub_desc(S, c)#, b-A@sub_desc(S, c)


print(A1@PCMMP2(A1, b1))
