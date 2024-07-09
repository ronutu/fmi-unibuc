n=1000

## MIRC pentru repartitia Poisson

lnf1 <- expression(log(lambda^x*exp(-lambda)/factorial(x)))    #logaritmam functia de repartitie Poissoin
deriv1 <- D(lnf1,'lambda')                                     #derivara 1 a functiei de mai sus
deriv2 <- D(deriv1,'lambda')                                   #derivata a 2-a a functiei de mai sus


frcpois <- function(n,lambda,esantion) {
  
  derivata2 <- function(lambda,esantion) {
    (lambda^((esantion - 1) - 1) * (esantion - 1) * esantion * exp(-lambda) - 
       lambda^(esantion - 1) * esantion * exp(-lambda) - (lambda^(esantion - 1) * esantion * exp(-lambda) - 
        lambda^esantion * exp(-lambda)))/factorial(esantion)/(lambda^esantion * exp(-lambda)/factorial(esantion)) - 
      (lambda^(esantion - 1) * esantion * exp(-lambda) - lambda^esantion * exp(-lambda))/factorial(esantion) * 
      ((lambda^(esantion - 1) * esantion * exp(-lambda) - lambda^esantion * exp(-lambda))/factorial(esantion))/(lambda^esantion * 
                                                                                               exp(-lambda)/factorial(esantion))^2
  }   
  
  
  #rezultatul derivatei a doua
  
  MIRC <- 1/(-n*mean(eval(derivata2(lambda,esantion))))
  return(MIRC)
}

#
#

#Exemplu

X <- rpois(n,1)
MIRC <- frcpois(n,1,X)

#
#

## MIRC pentru repartitia Exponentiala
n=1000

lnf2<- expression(log(lambda*exp(-lambda*x)))         #logaritmam functia de repartitie Exponentiala

deriv1 <- D(lnf2,'lambda')                            #derivata 1 a functiei de mai sus
deriv2 <- D(deriv1,'lambda')                          #derivata a 2-a a functiei de mai sus

frcexp <- function(n,esantion,lambda) {
  
  derivata2 <- function(lambda,esantion) {
    
    -((exp(-lambda * esantion) * esantion + ((exp(-lambda * esantion) * esantion) - lambda * 
                                               (exp(-lambda * esantion) * esantion * esantion)))/(lambda * exp(-lambda * esantion)) + 
        (exp(-lambda * esantion) - lambda * (exp(-lambda * esantion) * esantion)) * (exp(-lambda * esantion) - 
                                              lambda * (exp(-lambda * esantion) * esantion))/(lambda * exp(-lambda * esantion))^2)
  }   
  
  #rezultatul derivatei a doua 
  
  MIRC <- 1/(-n*mean(eval(derivata2(lambda,esantion))))
  return(MIRC)
}

#
#

#Exemplu

X <- rexp(n)
MIRC <- frcexp(n,X,1)