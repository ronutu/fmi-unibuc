n <- 100


rlogistic <- function(n,miu,beta){
  U <- runif(n)
  X <- miu+beta*log(U)-beta*log(1-U)           #inversa functiei de repartitie
  return(X)
}

g <- rlogistic(n,0,1) 
L <- 1;
beta <- 10;

ver1 <- function(miu)
{
  for(i in 1:n)
  {
     L <- L*exp(-(g[i]-miu)/beta)/beta*(1+exp(-(g[i]-miu)/beta))^2;
  }
  return(L)
}


plot(ver1, col="red")
miu_optim1 <- optimise(ver1,lower=0,upper=1)


rCauchy1 <- function(n,miu,sigma){
  U <- runif(n)
  X <- miu+sigma*tan(pi*(2*U-1/2))
  return(X)
}


f <- rCauchy1(n,0,1)
sigma <- 1;

ver2 <- function(miu){
  for(i in 1:n){
    L <- L*(1/(pi*sigma))*1/(1+((f[i]-miu)/sigma)^2)
  }
  return(L)
}

plot(ver2, col="red")
miu_optim2 <- optimise(ver2,lower=0,upper=1)

