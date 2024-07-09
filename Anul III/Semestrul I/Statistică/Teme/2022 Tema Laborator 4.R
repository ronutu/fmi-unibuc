#exc 1 
exc_1 <- function(n,k)
{
  u = runif(n)  #generăm un vector uniform
  x <- u^(1/k)  #funcția găsită pentru exc 1
  return(x)
}
#afișăm și derivata să vedem cât de asemănătoare e histograma
dF1 <- function(x,k)
{
  x <- k*x^(k-1)
}

n <- 10^6
k <- 4  #dăm o valoare pentru a vedea histograma
y <- exc_1(n,k)
hist(y)
hist(y, col = 'purple', freq = F)
t <- seq(min(y),max(y),0.001)
lines(t,dF1(t,k),col='yellow',lwd = 2)

#exc 2 
exc_2 <- function(n,k)
{
  u = runif(n)  #generăm un vector uniform
  x <- (-1+(1+8*u)^(1/2))/2  #funcția găsită pentru exc 2
  return(x)
}
#afișăm și derivata să vedem cât de asemănătoare e histograma
dF2 <- function(x,k)
{
  x <- x+1/2
}

n <- 10^6
y <- exc_2(n,k)
hist(y)
hist(y, col = 'purple', freq = F)
t <- seq(min(y),max(y),0.001)
lines(t,dF2(t,k),col='yellow',lwd = 2)

#exc 3 
exc_3 <- function(n,k,a,b)
{
  u = runif(n)  #generăm un vector uniform
  x <- (log(u)/-a)^(1/b)  #funcția găsită pentru exc 3
  return(x)
}

n <- 10^6
a <- 3
b <- 5
y <- exc_3(n,k,a,b)
hist(y)
hist(y, col = 'purple', freq = F)

#exc 5 se produc valori not a number în funcție. 
exc_5 <- function(n,b)
{
  u = runif(n)  #generăm un vector uniform
  x <- sqrt(log(u)^(b))   #funcția găsită pentru exc 5
  return(x)
}

n <- 10^6
b <- 3
y <- exc_5(n,b)
hist(y)
hist(y, col = 'purple', freq = F)


#exc 6 aici cred că trebuie luat altfel u pentru a rămâne în domeniu
exc_6 <- function(n,k)
{
  u = runif(n)  #generăm un vector uniiform
  x <- tan(pi*(u-1/2))
  return(x)
}

n <- 10^6
y <- exc_6(n,k)
hist(y)
hist(y, col = 'purple', freq = F)
