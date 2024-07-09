# Ex. 1
f <- function(x) {
  x^6 * exp(-3*x)
}
n <- 10^7
x <- runif(n, min = 0, max = 10^4)
y <- f(x)
integrala <- mean(y)*10^4
cat(integrala)

# Ex. 2
f <- function(x) {
  x^7 * exp(-x^2)
}
n <- 10^7
x <- runif(n, min = 0, max = 10^4)
y <- f(x)
integrala <- mean(y)*10^4
cat(integrala)

# Ex. 3
f <- function(x) {
  (x-x^2)^5
}
n <- 10^7
x <- runif(n)
y <- f(x)
integrala <- mean(y)
cat(integrala)

# Ex. 4
f <- function(x) {
  2*x^4 * exp(-x^2)
}
n <- 10^7
x <- runif(n, min = 0, max = 10^4)
y <- f(x)
integrala <- mean(y)*10^4
cat(integrala)

# Ex. 5
f <- function(x) {
  sqrt(x-x^2)
}
n <- 10^7
x <- runif(n)
y <- f(x)
integrala <- mean(y)
cat(integrala)

# Ex. 6
f <- function(x) {
  1/((x^5*(1-x))^(1/6))
}
n <- 10^7
x <- runif(n)
y <- f(x)
integrala <- mean(y)
cat(integrala)

# Ex. 7
f <- function(x) {
  x^2 * sqrt(4-x^2)
}
n <- 10^7
x <- runif(n, min = 0, max = 2)
y <- f(x)
integrala <- mean(y)*2
cat(integrala)

# Ex. 8
f <- function(x) {
  x*(log(x))^5
}
n <- 10^7
x <- runif(n)
y <- f(x)
integrala <- mean(y)
cat(integrala)

# Ex. 9
f <- function(x) {
  1/sqrt((3-x) * (x-1))
}
n <- 10^7
x <- runif(n, min = 1, max = 3)
y <- f(x)
integrala <- mean(y)*2
cat(integrala)

# Ex. 10
f <- function(x) {
  sqrt(log(1/x))
}
n <- 10^7
x <- runif(n)
y <- f(x)
integrala <- mean(y)
cat(integrala)

# Ex. 11
f <- function(x) {
  (sin(x))^3 * (cos(x))^5
}
n <- 10^7
x <- runif(n, min = 0, max = pi/2)
y <- f(x)
integrala <- mean(y)*(pi/2)
cat(integrala)

# Ex. 12
f <- function(x) {
  x^6*sqrt(16-x^2)
}
n <- 10^7
x <- runif(n, min = -4, max = 0)
y <- f(x)
integrala <- mean(y)*4
cat(integrala)

# Ex. 13
f <- function(x) {
  x^2/(1+x^4)
}
n <- 10^7
x <- runif(n, min = 0, max = 10^4)
y <- f(x)
integrala <- mean(y)*10^4
cat(integrala)

# Ex. 14
f <- function(x) {
  exp(-x^2 + 2*x - 4)
}
n <- 10^7
x <- runif(n, min = 1, max = 10^4)
y <- f(x)
integrala <- mean(y)*(10^4-1)
cat(integrala)

# Ex. 15
f <- function(x) {
  (1/x) * (log(x))^3 * (1-log(x))^4
}
n <- 10^7
x <- runif(n, min = 1, max = exp(1))
y <- f(x)
integrala <- mean(y)*(exp(1) - 1)
cat(integrala)






