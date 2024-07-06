import math

# Ex.3: (Aproximarea lui sin)
x = math.pi/2
N = 10
serie = x
termen = x
for k in range(1, N+1):
    termen *= -(x**2)/(2*k*(2*k+1))
    serie += termen
    err_abs = abs(termen)
    print(k, "{:.20f}\t{:.4e}".format(serie, err_abs))