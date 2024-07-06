import numpy as np
import math

# Ex.1:


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


L = np.array([[2, 0, 0], [-1, 4, 0], [-2, 4, 1]])
b = np.array([[2], [3], [3]])
x = sub_asc(L, b)
print("x=\n", x)
print("L*x=b\n", np.matmul(L, x))

# Ex.2:


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


U = np.array([[2, -1, -2], [0, 4, 4], [0, 0, 1]])
b = np.array([[-1], [8], [1]])
x = sub_desc(U, b)

print("x=\n", x)
print("U*x=b\n", np.matmul(U, x))


# # Ex.3: (Aproximarea lui cos)
# n = 10
# for x in [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, (2*math.pi)/3, (3*math.pi)/4, (5*math.pi)/6, math.pi]:
#     serie = 1
#     termen = 1
#     for k in range(1, n):
#         termen *= -(x ** 2) / ((2*k-1)*2*k)
#         serie += termen
#         err_abs = abs(serie-math.cos(x))
#         err_relativa = abs(serie-math.cos(x))/abs(math.cos(x))
#         print("Pentru x = " + str(x) + " aproximarea lui cos(x) este: " + str(serie) + " iar valoarea lui cos(x) este: "+str(math.cos(x)))
#         print(colored("Erorile absolute si relative sunt: " + str(err_abs) + " si " + str(err_relativa), "yellow"))
