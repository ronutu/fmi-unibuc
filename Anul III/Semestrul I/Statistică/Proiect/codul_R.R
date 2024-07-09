#Proiect statistica
#Grupa312
#CÎRCIUMARU RAUL
#ONUȚU RADU-CONSTANTIN 
#PANĂ ALEXANDRA-IOANA
#VLAD MARIANA-CRISTINA


# Ex. 1
# 1)
# Binomiala
binomModif <- function(nr = 1000, p = 0.1, n = 1000){
  x_values <- rbinom(n, size = nr, prob = p)
  Xn_bar <- mean(x_values)
  miu <- n * p  # Media E(X1)
  sigma <- sqrt(n * p * (1 - p))  # sqrt(Varianta)
  
  Zn1 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn1 <- binomModif(1000, 0.1)
x <- 1

cat("P(Z_n <= 1):", pnorm(Zn1, x))


# Geometrica
geomModif <- function(p, n = 1000){
  x_values <- rgeom(n, prob = p)
  Xn_bar <- mean(x_values)
  miu <- 1/p  # Media E(X1)
  sigma <- sqrt((1-p)/p^2)  # sqrt(Varianta)
  Zn2 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn2 <- geomModif(0.01)
x <- 1/2

cat("P(Z_n <= 1/2):", pnorm(Zn2, x))


# Poisson
poisModif <- function(lbd, n = 1000){
  x_values <- rpois(n, lambda = lbd)
  Xn_bar <- mean(x_values)
  miu <- lbd  # Media E(X1)
  sigma <- sqrt(lbd)  # sqrt(Varianta)
  
  Zn3 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn3 <- poisModif(3)
x <- 1/2

cat("P(Z_n <= 1/2):", pnorm(Zn3, x))


# Uniforma discreta
unifDiscModif <- function(n = 1000){
  x_values <- runif(n)
  Xn_bar <- mean(x_values)
  miu <- 1/2  # Media E(X1)
  sigma <- 1/2  # sqrt(Varianta)
  
  Zn4 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn4 <- unifDiscModif()
x <- 0

cat("P(Z_n <= 0):", pnorm(Zn4, x))


# Uniforma continua
unifContModif <- function(n = 1000){
  x_values <- runif(n)
  Xn_bar <- mean(x_values)
  miu <- 1/2  # Media E(X1)
  sigma <- sqrt(1/12)  # sqrt(Varianta)
  
  Zn5 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn5 <- unifContModif()
x <- 0

cat("P(Z_n <= 0):", pnorm(Zn5, x))


# Exponentiala
expModif <- function(lbd, n = 1000){
  x_values <- rexp(n, rate = 1)
  Xn_bar <- mean(x_values)
  miu <- 1/lbd  # Media E(X1)
  sigma <- 1/lbd  # sqrt(Varianta)
  
  Zn6 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn6 <- expModif(1)
x <- 0

cat("P(Z_n < 0):", pnorm(Zn6, x))


# Gamma
gammaModif <- function(alpha, beta, n = 1000){
  x_values <- rgamma(n, shape = alpha, rate = beta)
  Xn_bar <- mean(x_values)
  miu <- alpha/beta  # Media E(X1)
  sigma <- sqrt(alpha/beta^2)  # sqrt(Varianta)
  
  Zn7 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn7 <- gammaModif(2, 5)
x <- 0

cat("P(Z_n < 0):", pnorm(Zn7, x))

# Beta
betaModif <- function(alpha, beta, n = 1000){
  x_values <- rbeta(n, shape1 = alpha, shape2 = beta)
  Xn_bar <- mean(x_values)
  miu <- alpha/(alpha + beta)  # Media E(X1)
  sigma <- sqrt((alpha*beta)/((alpha+beta)^2*(alpha + beta + 1)))  # sqrt(Varianta)
  
  Zn8 <- (sqrt(n)*(Xn_bar - miu))/sigma
}

Zn8 <- betaModif(2, 5)
x <- 0

cat("P(Z_n < 0):", pnorm(Zn8, x))


#-------------------------------------------------------------------------------
# 2)
# Am rulat pe rand fiecare repartitie si dupa am rulat codul de mai jos
plot(c(1:1000), (sqrt(c(1:1000))*(Xn_bar - miu))/sigma, type = "l",
     col = "magenta", xlab = "n", ylab = "Zn", main = "Beta")


#-------------------------------------------------------------------------------
# 3)
# La dummyFunction se modifica in functie de caz
dummyFunction <- function(a,b){
  binomModif(1000, 0.1)
}

dif <- function(x){
  mesaj <- "Introduceti nr funtiei pe care o doriti executata: 
1.⁠ ⁠Binomiala
2.⁠ ⁠Geometrica
3.⁠ ⁠Poisson
4.⁠ ⁠Uniforma pe caz discret
5.⁠ ⁠Uniforma pe caz continuu
6.⁠ ⁠Exponentiala
7.⁠ ⁠Gamma
8.⁠ ⁠Beta"
  input_utilizator <- readline(prompt = mesaj)
  if(input_utilizator == "1"){
    print(binomModif(1000, 0.1) - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else if (input_utilizator == "2") {
    print(geomModif(0.1) - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else if (input_utilizator == "3"){
    print(poisModif(3) - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else if (input_utilizator == "4"){
    print(unifDiscModif() - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else if (input_utilizator == "5"){
    print(unifContModif() - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else if (input_utilizator == "6"){
    print(expModif(1) - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else if (input_utilizator == "7"){
    print(gammaModif(2,5) - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else if (input_utilizator == "8"){
    print(betaModif(2,5) - (exp(-(x^2)/2))/(sqrt(2*pi)))
    optimise(dummyFunction, c(0, 1000), maximum = TRUE)[1]
  } else {
    print("Invalid Input!")
  }
}
dif(1)
optimise(Zn_8, c(0, 1000), maximum=TRUE)[1]


#-------------------------------------------------------------------------------
# 4)
# Functii pentru E(X) si Var(X)
medie_discret <- function(variabila,densitatea)
{
  E <- sum(variabila*densitatea)
}
medie_continuu <- function(variabila, fct_masa)
{
  E <- integrate(function(x) {x * fct_masa(x)}, -Inf, Inf)$value
}

varianta_discret <- function(variabila, densitate, medie)
{
  Var <- sum(variabila^2 * densitate) - sum(variabila * densitate)^2  
}

varianta_continuu <- function(variabila, fct_masa, medie)
{
  Var <- integrate(function(x) {x^2 * fct_masa(x)}, -Inf, Inf)$value - medie^2
}


#exemplu discret
var <- c(2,4,8,6)
densitate<- c(0.1, 0.8, 0.8, 0.3)
E <- medie_discret(var,densitate)
Var <- varianta_discret(var,E)
cat("E(X)=", E)
cat("Var(X)=", Var)

#exemplu continuu
var <- c(2,4,8,6)
f <- function(x) ifelse(x>=0 & x<1, 5*(2*x^2+1)/3,0)
fct_masa<- function(x) ifelse(x>=0 & x<=1, 5*(2*x^2+1)/3,0)
E <- medie_continuu(var, fct_masa)
Var <- varianta_continuu(var, fct_masa,E)
cat("E(X)=", E)
cat("Var(X)=", Var)


#-------------------------------------------------------------------------------
# 5)
medie_discret2 <- function(variabila,densitate)
{
  E <- medie_discret(variabila,densitate)
  E2 <- sum(abs(variabila - E)^3 * densitate) 
  return (E2)
}
medie_continuu2 <- function(variabila, fct_masa)
{
  E <- medie_continuu(variabila, fct_masa)
  E2 <- integrate(function(x) {abs(x - E)^3 * x * fct_masa(x)}, -Inf, Inf)$value
  return (E2)
}

#exemplu discret
var <- c(2,4,8,6)
densitate <- c(0.1, 0.2, 0.3, 0.4)
E2 <- medie_discret2(var, densitate)
cat("E2(X)=", E2)

# exemplu continuu
var <- c(2,4,8,6)
f <- function(x) ifelse(x>=0 & x<1, 5*(2*x^2+1)/3,0)
fct_masa<- function(x) ifelse(x>=0 & x<=1, 5*(2*x^2+1)/3,0)
E2 <- medie_continuu2(var,fct_masa)
cat("E2(X)=", E2)


#-------------------------------------------------------------------------------
# 6)
marginea_discret <- function(variabila,densitate, n)
{
  E <- medie_discret(variabila,densitate)
  numarator <- sum(abs(variabila - E)^3 * densitate)
  Var <- sum(variabila^2 * densitate) - sum(variabila * densitate)^2 
  numitor <- sqrt(n)*(Var^(3/2))
  
  return ((33*numarator)/(4*numitor))
}

marginea_continuu <- function(variabila, fct_masa,n)
{
  E <- medie_continuu(variabila, fct_masa)
  numarator <- integrate(function(x) {abs(x - E)^3 * x * fct_masa(x)}, -Inf, Inf)$value
  # Var e functia de la ex. 4
  Var <- integrate(function(x) {x^2 * fct_masa(x)}, -Inf, Inf)$value - E^2
  numitor <- sqrt(n)*(Var^(3/2))
  return ((33*numarator)/(4*numitor))
}
fct_masa_exponentiala <- function(x) {dexp(x, rate = 0.7)}
fct_masa_gamma <- function(x) {dgamma(x, shape = 2, scale = 1)}
fct_masa_beta <- function(x) {dbeta(x, shape1 = 2, shape2 = 4)}

df <- data.frame (
  nume_repartitie = c("Binomiala", "Geometrica", "Poisson", "Uniforma discreta"
                      , "Uniforma continua", "Exponentiala", "Gamma", "Beta"),
  marginea_sup_30 = c(marginea_discret(1:30, dbinom(1:30, 30, 0.4), 30),#binomiala 
                      marginea_discret(1:30, dgeom(1:30, prob = 0.7), 30), #Geometrica
                      marginea_discret(1:30, dpois(1:30, 2), 30),#Poisson
                      marginea_discret(1:30, rep(1/30, 30), 30),#Uniforma discreta
                      marginea_continuu(seq(0, 1, length.out = 30), dunif, 30), #Uniforma continua
                      marginea_continuu(seq(0, 10, length.out = 30), fct_masa_exponentiala, 30), #Exponentiala
                      marginea_continuu(seq(0, 10, length.out = 30), fct_masa_gamma, 30), #Gamma
                      marginea_continuu(seq(0, 1, length.out = 30), fct_masa_beta, 30)#Beta
  ),
  marginea_sup_100 = c(marginea_discret(1:100, dbinom(1:100, 100, 0.4), 100),#binomiala 
                       marginea_discret(1:100, dgeom(1:100, prob = 0.7), 100), #Geometrica
                       marginea_discret(1:100, dpois(1:100, 2), 100),#Poisson
                       marginea_discret(1:100, rep(1/100, 100), 100),#Uniforma discreta
                       marginea_continuu(seq(0, 1, length.out = 100), dunif, 100), #Uniforma continua
                       marginea_continuu(seq(0, 10, length.out = 100), fct_masa_exponentiala, 100), #Exponentiala
                       marginea_continuu(seq(0, 10, length.out = 100), fct_masa_gamma, 100), #Gamma
                       marginea_continuu(seq(0, 1, length.out = 100), fct_masa_beta, 100)#Beta
  ),
  marginea_sup_1000 = c(marginea_discret(1:1000, dbinom(1:1000, 1000, 0.4), 1000),#binomiala 
                        marginea_discret(1:1000, dgeom(1:1000, prob = 0.7), 1000), #Geometrica
                        marginea_discret(1:1000, dpois(1:1000, 2), 1000),#Poisson
                        marginea_discret(1:1000, rep(1/1000, 1000), 1000),#Uniforma discreta
                        marginea_continuu(seq(0, 1, length.out = 1000), dunif, 1000), #Uniforma continua
                        marginea_continuu(seq(0, 10, length.out = 1000), fct_masa_exponentiala, 1000), #Exponentiala
                        marginea_continuu(seq(0, 10, length.out = 1000), fct_masa_gamma, 1000), #Gamma
                        marginea_continuu(seq(0, 1, length.out = 1000), fct_masa_beta, 1000)#Beta
  )
)

df


#-------------------------------------------------------------------------------
# 7)
repModif<- function(x) {
  t <- 1
  binomModif(1000, 0.1) - (exp(-(t^2)/2))/(sqrt(2*pi))
}
lista_n = c(1:1000)

repModif <- function(x) {
  t <- 1
  geomModif(0.01) - (exp(-(t^2)/2))/(sqrt(2*pi))
}
repModif <- function(x) {
  t <- 1
  poisModif(3) - (exp(-(t^2)/2))/(sqrt(2*pi))
}
repModif <- function(x) {
  t <- 1
  unifDiscModif()- (exp(-(t^2)/2))/(sqrt(2*pi))
}
repModif <- function(x) {
  t <- 1
  unifContModif()- (exp(-(t^2)/2))/(sqrt(2*pi))
}
repModif <- function(x) {
  t <- 1
  expModif(1)- (exp(-(t^2)/2))/(sqrt(2*pi))
}
repModif <- function(x) {
  t <- 1
  gammaModif(2, 5)- (exp(-(t^2)/2))/(sqrt(2*pi))
}
repModif <- function(x) {
  t <- 1
  betaModif(2, 5) - (exp(-(t^2)/2))/(sqrt(2*pi))
}
lista_n = c(1:1000)
y = sapply(lista_n, repModif)
plot(lista_n,y)



#-------------------------------------------------------------------------------
# 8)
margine_discret<- function(variabila, densitate) 
{
  E <- medie_discret( variabila, densitate)
  Var <- varianta_discret(variabila, densitate, E)
  E2 <- medie_discret2(variabila, densitate)
  margine <- 33/4*E2/(Var^3)
  return(margine)
}

margine_continuu<- function(variabila, fct_masa) 
{
  E <- medie_continuu( variabila, fct_masa)
  Var <- varianta_continuu(variabila, fct_masa, E)
  E2 <- medie_continuu2(variabila, fct_masa)
  margine <- 33/4*E2/(Var^3)
  return(margine)
}

#exemplu discret
var <- c(2,4,8,6)
densitate <- c(0.1, 0.2, 0.3, 0.4)
margine <- margine_discret(var, densitate)
cat("Margine=", margine)

#exemplu continuu
var <- c(2,4,8,6)
f <- function(x) ifelse(x>=0 & x<1, 5*(2*x^2+1)/3,0)
fct_masa <- function(x) ifelse(x>=0 & x<=1, 5*(2*x^2+1)/3,0)
margine <- margine_continuu(var, fct_masa)
cat("Margine=", margine)




#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Ex. II
# a)
h <- function(x) {
  return (exp(-x^2/2) * (sin((6*x)^2) + 3*cos(x^2)*sin((4*x)^2) + 1))
}

# u(x) = h(x)/g(x)
u <-  function(x) {
  return (sqrt(2*pi) * (sin((6*x)^2) + 3*cos(x^2) * (sin((4*x)^2) + 1)))
}

M <- optimise(u, c(0, 3, 0), maximum = TRUE)
cat("M =", M[[2]])
values <- seq(-3, 3, 0.005)

plot(values, h(values), type = "l", col = "magenta")
par(new = TRUE)  # folosim par pt. a pune mai multe ploturi pe acelasi grafic
plot(values, dnorm(values) * M[[2]], type = "l", col = "blue", yaxt = "n",
     xaxt = "n", xlab = "Valori", ylab = "h(Valori)")
axis(side = 4, at = pretty(M[[2]] * dnorm(values)),
     labels = pretty(M[[2]] * dnorm(values)), col = "blue", col.axis = "blue")


#-------------------------------------------------------------------------------
# b)
values_list <- c()
n = 25000
contor = 0
i = 1
while (i <= n) {
  u <-  runif(1, 0, 1)
  x <- rnorm(1, 0, 1)
  if (u <= h(x)/(M[[2]]*dnorm(x))) {
    values_list[contor] <- x
    contor <- contor+1
  }
  i <- i+1
}
values_list


#-------------------------------------------------------------------------------
# c)
rata_acceptare <- contor/n
cat("rata de acceptare =", rata_acceptare)

hist(values_list, breaks = 100, freq = FALSE, col = "magenta",
     xlab = "Valori acceptate", ylab = "Densitate",
     main = "Histograma valorilor acceptate", cex.main = 0.7)


normF <-  1/(M[[2]]*rata_acceptare)
cat("constanta pentru normalizarea functiei =", normF)
lines(values, normF*h(values), col = "green", type = "l")


require("ConvergenceConcepts")


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Ex. III
# 1)
genXnBeta <- function(n) {
  return (rbeta(n = n, shape1 = 1/n, shape2 = 1/n))
}

check.convergence(2000, 1000, genXnBeta, mode="L", density = F,
                  densfunc = function(x){dbinom(x, size = 1, prob = 1/2)},
                  probfunc = function(x){pbinom(x, size = 1, prob = 1/2)},
                  tinf = -2, tsup = 2)


genXnBeta <- function(n) {
  a <- runif(1, 0, 1000)
  b <- runif(1, 0, 1000)
  return (rbeta(n = n, shape1 = a/n, shape2 = b/n))
}

check.convergence(2000, 1000, genXnBeta, mode="L", density = F,
                  densfunc = function(x){dbinom(x, size = 1, prob = 1/2)},
                  probfunc = function(x){pbinom(x, size = 1, prob = 1/2)},
                  tinf = -2, tsup = 2)


#-------------------------------------------------------------------------------
# 2)
genXn <- function(n) {
  return (seq(1/n, 1, by=1/n))
}

check.convergence(2000, 1000, genXn, mode="L", density = F,
                  densfunc = function(x){dunif(x, min = 0, max = 1)},
                  probfunc = function(x){punif(x, min = 0, max = 1)},
                  tinf = -2, tsup = 2)


X <- runif(1)
check.convergence(2000, 500, genXn, mode="p")


#-------------------------------------------------------------------------------
# 3)
m = 0
M = 10^4
genXn <- function(n) {
  return (runif(n, min = m, max = M))
}

check.convergence(2000, 500, genXn, mode = "as")



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Ex. IV
# 1)
n <- 10^6
# a)
# v este vectorul care arata cate numere sunt castigatoare pe fiecare bilet
v <- rhyper(nn = n, m = 6, n = 43, k = 6)
cat("Probabilitatea de a castiga din prima incercare cu 3 numere castigatoare este:", sum(v==3)/n)
cat("Probabilitatea de a castiga din prima incercare cu 4 numere castigatoare este:", sum(v==4)/n)
cat("Probabilitatea de a castiga din prima incercare cu 5 numere castigatoare este:", sum(v==5)/n)
cat("Probabilitatea de a castiga din prima incercare cu 6 numere castigatoare este:", sum(v==6)/n)


#-------------------------------------------------------------------------------
# b)
k <- 10
v <- rhyper(nn = n, m = 6, n = 43, k = 6)

# Am luat doar primele k valori si am verificat daca este vreun bilet castigator acolo
cat("Probabilitatea de a castiga din k incercari cu 3 numere castigatoare este:", sum(v[0:k]==3)/n)
cat("Probabilitatea de a castiga din k incercari cu 4 numere castigatoare este:", sum(v[0:k]==4)/n)
cat("Probabilitatea de a castiga din k incercari cu 5 numere castigatoare este:", sum(v[0:k]==5)/n)
cat("Probabilitatea de a castiga din k incercari cu 6 numere castigatoare este:", sum(v[0:k]==6)/n)



#-------------------------------------------------------------------------------
# c)
k <- 1000
r <- 6
v <- rhyper(nn = n, m = 6, n = 43, k = 6)

prob3 <- dbinom(r, size = k, prob = (sum(v[0:k]==3)/k))
prob4 <- dbinom(r, size = k, prob = (sum(v[0:k]==4)/k))
prob5 <- dbinom(r, size = k, prob = (sum(v[0:k]==5)/k))
prob6 <- dbinom(r, size = k, prob = (sum(v[0:k]==6)/k))

cat("Probabilitatea de a castiga de r ori din k incercari cu 3 numere castigatoare este:", prob3)
cat("Probabilitatea de a castiga de r ori din k incercari cu 4 numere castigatoare este:", prob4)
cat("Probabilitatea de a castiga de r ori din k incercari cu 5 numere castigatoare este:", prob5)
cat("Probabilitatea de a castiga de r ori din k incercari cu 6 numere castigatoare este:", prob6)



#-------------------------------------------------------------------------------
# d)
v <- rhyper(nn = n, m = 6, n = 43, k = 6)
r <- 1
k <- 2

prob3 <- mean(rnbinom(n = n, size = k, prob = sum(v==3)/n) == r)
prob4 <- mean(rnbinom(n = n, size = k, prob = sum(v==4)/n) == r)
prob5 <- mean(rnbinom(n = n, size = k, prob = sum(v==5)/n) == r)
prob6 <- mean(rnbinom(n = n, size = k, prob = sum(v==6)/n) == r)

cat("Probabilitatea de a castiga de r ori dupa k esecuri cu 3 numere castigatoare este:", prob3)
cat("Probabilitatea de a castiga de r ori dupa k esecuri cu 4 numere castigatoare este:", prob4)
cat("Probabilitatea de a castiga de r ori dupa k esecuri cu 5 numere castigatoare este:", prob5)
cat("Probabilitatea de a castiga de r ori dupa k esecuri cu 6 numere castigatoare este:", prob6)


#-------------------------------------------------------------------------------
# e)
# Intr-un an sunt 52 de sapt.
v <- rhyper(nn = 52, m = 6, n = 43, k = 6)
p = sum(v>=3)/52
f <- function(v) {
  sum(v>=3)/52
}
vect <- sapply(v, f)
media <- mean(vect)
cat("Media de a castiga o data pe an timp de 30 de ani este:", media)


#-------------------------------------------------------------------------------
# f)
v <- rhyper(nn = 52, m = 6, n = 43, k = 6)
p <-  sum(v>=3)/52
prob_pierdere <-  1-p
cat("Probabilitaeta de a nu castiga intr-un an este:", prob_pierdere)


#-------------------------------------------------------------------------------
# 2)
# a)


#-------------------------------------------------------------------------------
# b)
# ne folosim de 1) a)
n <- 10^6
v <- rhyper(nn = n, m = 6, n = 43, k = 6)


# nr = nr de jucatori la o extragere
nr <- 0.6

# s = suma castigata de loterie intr-un an
s <- 104*7*nr


# s3 = suma de bani pierduta de loterie pentru cei care au 3 numere castigatoare
s3 <- nr*(sum(v==3)/n)*30

s4 <- (sum(v==4)/n) * 363350

s5 <- (sum(v==5)/n) * 390000

s6 <- (sum(v==6)/n) * 1090000

profit <- s - (s3+s4+s5+s6)


cat("Numar de bilete minime", 104*nr)
cat("Profit", profit)


#-------------------------------------------------------------------------------
# c)
# Cazul in care luam 10 bilete simple
prob <- 1 - (1-(sum(v>=3)/n))^10
cat("Probabilitatea cu 10 bilete simple:", prob)

# Cazul in care luam 1 bilet compus (7 numere) si 3 bilete simple
v1 <- rhyper(nn = n, m = 6, n = 43, k = 7)
prob1 <- sum(v1>=3)/n
prob1


prob2 <- 1 - (1-(sum(v>=3)/n))^3
prob2

# Aplic P(prob1 U prob2) = P(prob1) + P(prob2) - P(prob1 n prob2)

prob_finala <- prob1 + prob2 - prob1*prob2
cat("Probabilitatea cu 1 bilet compus si 3 bilete simple:", prob_finala)


#-------------------------------------------------------------------------------
# d)
# Repartitia asociata este cea binomiala (numarul de incercari = numarul de 
# jucatori de la o extragere)

# Media uneri repartitii binomiale este n*p

nr <- 1000   # nr de jucatori
media3 <- nr * (sum(v==3)/n)
media4 <- nr * (sum(v==4)/n)
media5 <- nr * (sum(v==5)/n)
media6 <- nr * (sum(v==6)/n)

cat("Numarul mediu de castigatori de la categoria de 3 numere:", media3)
cat("Numarul mediu de castigatori de la categoria de 4 numere:", media4)
cat("Numarul mediu de castigatori de la categoria de 5 numere:", media5)
cat("Numarul mediu de castigatori de la categoria de 6 numere:", media6)



#-------------------------------------------------------------------------------
# 3)
# a)
# Cel mai prost caz posibil
# Iau primele 6 numere de ex
v3 <- rhyper(nn = n, m = 6, n = 42, k = 6)

# Cel mai bun caz posibil
# Cazul optim = cazul in care alegi numere care nu sunt in margini si care nu sunt vecine
v2 <- rhyper(nn = n, m = 6, n = 9, k = 6)


# Media de probabilitati dintre cel mai bun caz si cel mai prost
media <- (sum(v3>=3)/n + sum(v2>=3)/n)/2

c <- media/(sum(v>=3)/n)
pret_optim <- c*7
cat("Pretul biletului a.i. jucatorii sa fie interesati este:", c*7)


#-------------------------------------------------------------------------------
# b)
v <- rhyper(nn = n, m = 6, n = 43, k = 6)
cat("Probabilitatea de a castiga la un bilet simplu", sum(v>=3)/n)
v2 <- rhyper(nn = n, m = 6, n = 9, k = 6)
cat("Probabilitatea de a castiga la un bilet stanga-dreapta in cazul optim", sum(v2>=3)/n)

# Impartim probabilitea de la biletul simplu cu cea de la biletul s-d
c <- (sum(v2>=3)/n)/( sum(v>=3)/n)

# Inmultim pretul unui biletu simplu cu c
pret_bilet_sd <- c*7
cat("Pretul minim pentru un bilet s-d este", pret_bilet_sd)


#-------------------------------------------------------------------------------
# c)
install.packages("animation")
library(animation)

interes <- function(price) {
  interes_cumparator <- 100 - price
  interes_loterie <- price
  return(list(interes_cumparator, interes_loterie))
}

pret <- seq(50, 150, by = 5)

data_list <- lapply(pret, interes)
interes_cumparator <- sapply(data_list, "[[", 1)
interes_loterie <- sapply(data_list, "[[", 2)


ani.options(interval = 0.5)
saveGIF({
  for (i in 1:length(pret)) {
    plot(pret, interes_cumparator, type = "l", ylim = c(0, 100), col = "blue", xlab = "Pret", ylab = "Interes")
    lines(pret, interes_loterie, type = "l", col = "red")
    points(pret[i], interes_cumparator[i], col = "blue", pch = 19, cex = 1.5)
    points(pret[i], interes_loterie[i], col = "red", pch = 19, cex = 1.5)
    legend("topright", legend = c("Client", "Loterie"), col = c("blue", "red"), lty = 1, cex = 0.8)
    ani.pause()
  }
})


#-------------------------------------------------------------------------------
# d)
# Strategia: Alegem numerele care nu sunt la margine si care nu sunt vecine intre ele
v2 <- rhyper(nn = n, m = 6, n = 9, k = 6)
cat("Probabilitatea de castig este:", sum(v2>=3)/n)



#-------------------------------------------------------------------------------
# e)
# Un jucator plateste pe an numai pe bilete 104x7 lei = 728 lei


v <- rhyper(nn = n, m = 6, n = 43, k = 6)
# Castigul estimat anual este de:
castig <- (sum(v>=3)/n)* 7*104

cat("Un jucator de bilete simple castiga anual:", castig-728)


#-------------------------------------------------------------------------------
# 4)

# Ultimii 20 de ani inseamna 104 extrageri pe an x 20 de ani
sim_extrageri <- floor(runif(104*20, min = 1, max = 49))

tabel_frecventa <- table(sim_extrageri)

barplot(tabel_frecventa, xlab = "Numere", ylab = "Frecventa")

# Ne uitam pe grafic si vedem care sunt cele mai putin extrase numere
# pentru ca teoretic numerele au aceeasi probabilitate de a pica
# adica o repartitie uniforma





