# Tema 3 (Simularea v.a.)
# Onutu Radu
# Grupa 312

# Ex. 1
n <- 2
inverse_F <- function(u) {
  u^(1/n)
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# Ex. 2
inverse_F <- function(u) {
  (-1+sqrt(1+8*u))/2
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# Ex. 3
a <- 2
b <- 3
inverse_F <- function(u, a, b) {
  (-(log(1-u)/a))^(1/b)
}
u <- runif(1000)
x <- inverse_F(u, a, b)
hist(x, freq=F)

# Ex. 4
inverse_F <- function(u) {
  if (0 <= u & u < 1/2) {
    return(2*u)
  } else if (1/2 <= u & u < 1) {
    return(4*u)
  }
}
u <- runif(1000)
x <- sapply(u, inverse_F)
hist(x, freq=F)

# Ex. 5
inverse_F <- function(u, b) {
  sqrt(-b*log(1-u))
}
b <- 2
u <- runif(1000)
x <- inverse_F(u, b)
hist(x, freq=F)

# Ex. 6
inverse_F <- function(u) {
  tan(pi*u - pi/2)
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# Ex. 7
inverse_F <- function(u) {
  log(tan((pi*u)/2))
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# Ex. 9
a <- 2
inverse_F <- function(u, a) {
  if (0 <= u & u < 1/2) {
    return((a*u + sqrt(a^2*u^2 + 4*a^2*u))/2)
  } else if (1/2 <= u & u < 1) {
    return((-a + u*a + a*sqrt(5-6*u+u^2))/(2-2*u))
  }
}
u <- runif(1000)
x <- sapply(u, inverse_F, a=a)
hist(x, freq=F)

# Ex. 10
inverse_F <- function(u) {
  exp(2*u - 1)
}
u <- runif(1000)
x <- sapply(u, inverse_F)
hist(x, freq=F)

# Ex. 11
inverse_F <- function(u) {
  2*u^2 + 1
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# Ex. 12
# a)
a <- 0.5
n <- 100
val <- numeric(1000)
i <- 1
while (i <= 1000) {
  x <- rexp(n, rate = a)
  val[i] <- max(x)
  i <- i+1
}
hist(val, freq=F)

# b)
a <- 0.5
n <- 100
val <- numeric(1000)
i <- 1
while (i <= 1000) {
  x <- rexp(n, rate = a)
  val[i] <- min(x)
  i <- i+1
}
hist(val, freq=F)

# 13
# a)
lambda <- 2
n <- 5
val <- numeric(1000)
i <- 1
while (i <= 1000) {
  x <- rpois(n, lambda)
  val[i] <- max(x)
  i <- i+1
}
hist(val, freq=F)

# b)
p <- 0.2
n <- 5
val <- numeric(1000)
i <- 1
while(i <= 1000) {
  x <- rbinom(n, 1, p)
  val[i] <- max(x)
  i <- i+1
}
hist(val, freq=F)

# c)
n <- 100
p <- 0.5
val <- numeric(1000)
i <- 1
while(i <= 1000) {
  x <- rbinom(n, size = n, prob = p)
  val[i] <- max(x)
  i <- i+1
}
hist(val, freq=F)

# 14
# a)
lambda <- 0.5
n <- 10
val <- numeric(1000)
i <- 1
while (i <= 1000) {
  x <- rexp(n, rate=lambda)
  val[i] <- sum(x)
  i <- i+1
}
hist(val, freq=F)

# b)
lambda <- 2
n <- 100
val <- numeric(1000)
i <- 1
while (i <= 1000) {
  x <- rpois(n, lambda=lambda)
  val[i] <- sum(x)
  i <- i+1
}
hist(val, freq=F)

# c)
n <- 100
val <- numeric(1000)
p <- 0.3
i <- 1
while (i <= 1000) {
  x <- rbinom(n, size=10, prob=p)
  val[i] <- sum(x)
  i <- i+1
}
hist(val, freq=F)

# d)
p <- 0.2
n <- 100
val <- numeric(1000)
i <- 1
while (i <= 1000) {
  x <- rgeom(n, prob=p)
  val[i] <- sum(x)
  i <- i+1
}
hist(val, freq=F)

# e)
r <- 5
p <- 0.3
n <- 100
val <- numeric(1000)
i <- 1
while (i <= 1000) {
  x <- rnbinom(n, size = r, prob = p)
  val[i] <- sum(x)
  i <- i+1
}
hist(val, freq=F)

# 15
n <- 10
m <- 8
p <- 0.5
s <- 12
x1 <- rbinom(1000, n, p)
x2 <- rbinom(1000, m, p)
poz <- which(x1+x2==s)
val <- x1[poz]
hist(val, freq=F)

# 16
n <- 1000
lambda <- 2
x <- rpois(n, lambda)
y <- rexp(n, rate = 1)
hist(x, freq = F)
hist(y, freq = F)

# 17
n <- 1000
x <- rnorm(n, mean = 0, sd = sqrt(rexp(n, rate = 1)))
y <- rexp(n, rate = 1)
hist(x, freq = F)
hist(y, freq = F)

# 18
n <- 1000
a1 <- 2
b1 <- 5
a2 <- 3
b2 <- 4
x1 <- rbeta(n, a1, b1)
x2 <- rbeta(n, a2, b2)
x <- x1*x2
hist(x, freq = F)

# 19
# a)
n <- 1000
x1 <- rnorm(n, mean = 0, sd = 1)
x2 <- rnorm(n, mean = 0, sd = 1)
x <- (x1-x2)/sqrt(2)
hist(x, freq = F)

# b)
n <- 1000
x1 <- rnorm(n, mean = 0, sd = 1)
x2 <- rnorm(n, mean = 0, sd = 1)
x3 <- rnorm(n, mean = 0, sd = 1)
x <- (x1+x2-2*x3)/sqrt(6)
hist(x, freq = F)

# c)
n <- 1000
x1 <- rnorm(n, mean = 0, sd = 1)
x2 <- rnorm(n, mean = 0, sd = 1)
x3 <- rnorm(n, mean = 0, sd = 1)
x <- (x1+x2+x3)/sqrt(3)
hist(x, freq = F)

# 20
n <- 1000
u <- rexp(n, rate = 1)
v <- rexp(n, rate = 1)
x <- u/(u+v)
hist(x, freq = F)

# 21
n <- 1000
x1 <- rnorm(n, mean = 0, sd = 1)
x2 <- rnorm(n, mean = 0, sd = 1)
x3 <- rnorm(n, mean = 0, sd = 1)
x4 <- rnorm(n, mean = 0, sd = 1)
x <- x1*x2 + x3*x4
hist(x, freq = F)

# 22
n <- 1000
x1 <- rnorm(n, mean = 0, sd = 1)
x2 <- rnorm(n, mean = 0, sd = 1)
x <- sqrt(x1^2 + x2^2)
hist(x, freq = F)

# 23
rej <- function() {
  y <- runif(1)
  u <- runif(1)
  x <- -1
  while (x == -1) {
    if (u <= exp(y-1)) {
      x <- y
      return (x)
    }
    else {
      y <- runif(1)
      u <- runif(1)
    }
  }
}

n <- 1
val <- numeric(1000)
while (n <= 1000) {
  val[n] <- rej()
  n <- n+1
}
hist(val, freq = F)

# 24
inverse_F <- function(u) {
  if (0 <= u & u <= 1/4) {
    return(2+2*sqrt(u))
  } else if (1/4 < u & u <= 1) {
    return(6-2*sqrt(3-3*u))
  }
}
u <- runif(1000)
x <- sapply(u, inverse_F)
hist(x, freq=F)

# 25
inverse_F <- function(u) {
  if (0 < u & u < 1/2) {
    return(log(2*u)/2)
  } else if (1/2 <= u & u < 1) {
    return(-log(2-2*u)/2)
  }
}
u <- runif(1000)
x <- sapply(u, inverse_F)
hist(x, freq=F)

# 26
rej <- function() {
  y <- rexp(1, rate = 1/2)
  u <- runif(1)
  x <- -1
  while (x == -1) {
    if (u <= (y^2 * exp(2-y/2))/16) {
      x <- y
      return (x)
    }
    else {
      y <- rexp(1, rate = 1/2)
      u <- runif(1)
    }
  }
}

n <- 1
val <- numeric(1000)
while (n <= 1000) {
  val[n] <- rej()
  n <- n+1
}
hist(val, freq = F)

# 27
rej <- function() {
  y <- runif(1, min = 0.8, max = 1)
  u <- runif(1)
  x <- -1
  while (x == -1) {
    if (u <= 5^4 * u * (1-u)^3) {
      x <- y
      return (x)
    }
    else {
      y <- runif(1, min = 0.8, max = 1)
      u <- runif(1)
    }
  }
}

n <- 1
val <- numeric(1000)
while (n <= 1000) {
  val[n] <- rej()
  n <- n+1
}
hist(val, freq = F)

# 29
inverse_F <- function(u) {
  c <- (exp(1) - 1)/(exp(1) + 1)
  return (exp(u+log(c)))
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# 30
inverse_F <- function(u) {
  if (0 < u & u < 1/2) {
    return(-sqrt(-log(2*u)))
  } else if (1/2 <= u & u < 1) {
    return(sqrt(-log(2-2*u)))
  }
}
u <- runif(1000)
x <- sapply(u, inverse_F)
hist(x, freq=F)

# 31
inverse_F <- function(u) {
  if (0 <= u & u <= 1/2) {
    return(2*u)
  } else if (1/2 < u & u <= 1) {
    return(4*u)
  }
}
u <- runif(1000)
x <- sapply(u, inverse_F)
hist(x, freq=F)

# 32
inverse_F <- function(u) {
  return (tan(u*pi - pi/2))
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# 33
rej <- function() {
  a <- 2
  y <- rexp(1, rate = a)
  u <- runif(1)
  x <- -1
  while (x == -1) {
    if (u <= 1 - exp(-a*y)) {
      x <- y
      return (x)
    }
    else {
      y <- rexp(1, rate = a)
      u <- runif(1)
    }
  }
}

n <- 1
val <- numeric(1000)
while (n <= 1000) {
  val[n] <- rej()
  n <- n+1
}
hist(val, freq = F)

# 34
inverse_F <- function(u) {
  return (log(tan(pi*u/2)))
}
u <- runif(1000)
x <- inverse_F(u)
hist(x, freq=F)

# 36
inverse_F <- function(u) {
  theta <- 1
  if (0 < u & u < theta/2) {
    return(2*u/theta)
  } else if (theta/2 <= u & u <= (theta+1)/2) {
    return(2*u-theta+1)
  }
  else if ((theta+1)/2 < u & u < 1) {
    return((2*u-3*theta+1)/(1-u))
  }
}
u <- runif(1000)
x <- sapply(u, inverse_F)
hist(x, freq=F)














