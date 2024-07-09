expo <- function(n, lambda) {
  u <- runif(n)
  x <- -log(1 - u)/lambda
  return (x)
}

gammaa <- function(n, alpha, beta) {
  u <- runif(n)
  x <- (-1 / beta) * log(1 - u^(1/alpha))
  return(x)
}

# 1
# a)
inverse_F <- function(u, a) {
  -log(1-u+u*exp(-a))
}
n <- 10^6
a <- 3
u <- runif(n)
x <- inverse_F(u, a)
hist(x, freq=F)

# b1)
rej <- function() {
  a <- 1/2
  y <- expo(1, a)
  u <- runif(1)
  x <- -1
  while (x == -1) {
    if (u <= exp(-y/2)) {
      x <- y
      return (x)
    }
    else {
      y <- expo(1, a)
      u <- runif(1)
    }
  }
}

i <- 1
n <- 10^6
val <- numeric(1000)
while (i <= 1000) {
  val[i] <- rej()
  i <- i+1
}
hist(val, freq = F)

# b2)
rej <- function() {
  y <- runif(1)
  u <- runif(1)
  x <- -1
  while (x == -1) {
    if (u <= exp(-y)) {
      x <- y
      return (x)
    }
    else {
      y <- runif(1)
      u <- runif(1)
    }
  }
}

i <- 1
n <- 10^6
val <- numeric(1000)
while (i <= 1000) {
  val[i] <- rej()
  i <- i+1
}
hist(val, freq = F)

# 2
n <- 10^6
a <- 2
b <- 3
y1 <- gammaa(n, a, 1)
y2 <- gammaa(n, b, 1)

x <- y1 / (y1 + y2)

hist(x, freq=F)
curve(dbeta(x, a, b), add=T)

# 4
n <- 10^6
u <- (runif(n))^2
uu <- sqrt(1-u^2)
covarianta <- cov(u, uu)
cat(covarianta)



