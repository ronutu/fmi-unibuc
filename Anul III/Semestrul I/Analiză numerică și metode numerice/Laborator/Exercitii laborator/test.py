# ascendenta
f_deriv = (f(x+h[k-1]) - f(x))/h[k-1]

# descendenta
f_deriv = (f(x) - f(x-h[k-1]))/h[k-1]

# centrala
f_deriv = (f(x+h[k-1]) - f(x-h[k-1]))/(2*h[k-1])