  h=function(x){
    return (exp(-x^2/2)*(sin(6*x)^2+3*(cos(x^2))^2*(sin(4*x))^2+1))
  }
  valori=seq(-3,3,0.0005)
  plot(valori, h(valori), type="l", col="red")
  grid(nx=NULL, col="lightgray", lty="dotted",lwd=par("lwd"),equilogs=TRUE)
  
  raport = function(x) {
    return ( sqrt(2*pi) * ( sin(6*x)^2 + 3*(cos(x))^2 * (sin(4*x))^2 + 1) )
  }
  M = optimise(raport, c(-0.3,0), maximum = TRUE)
  M[2]
  
  raport = function(x) {
    return ( sqrt(2*pi) * ( sin(6*x^2) + 3*cos(x^2) * sin(4*x^2) + 1) )
  }
  M=optimise(raport, c(-0.3,0), maximum = TRUE)
  valori = seq(-3,3, 0.0005)
  plot(valori, h(valori), type="l", col = "dimgray")
  grid(nx = NULL, col = "lightgray", lty = "dotted",
       lwd = par("lwd"), equilogs = TRUE)
  lines(valori, dnorm(valori)*M[[2]], col = "red")
  
  ##
  ##
  
  valoriRetinute = c()
  n = 2500 #numar de incercari
  contor = 0 #numaram incercarile bune
  i = 1
  while( i <= n ) {
    u = runif(1,0,1) #generez o observatie din uniforma
    x = rnorm(1,0,1) #generez o observatie din normala standard
    if( u <= h(x)/(M[[2]]*dnorm(x))) {
      valoriRetinute[contor] = x
      contor = contor + 1
    }
    i=i + 1
  }
  #Astfel procentul de valori obtinute este:
  p = contor/n
  p
  M[[2]]*p #integrala lui h
  integrate(h, -Inf, Inf) 
  
  normF = 1/(M[[2]]*p) #calcuez valoarea aproximativa a constantei
  normF
  
  hist(valoriRetinute, breaks = 100, freq = FALSE, col = "turquoise",
       xlab = "Valori acceptate",
       ylab = "Densitate",
       main = "Histrograma valorilor acceptate",
       cex.main = 0.7) #histrograma valorilor acceptate
  lines(valori, normF*h(valori), col = "red", type="l") #graficul functiei normalizate
  grid(nx = NULL, col = "lightgray", lty = "dotted",
       lwd = par("lwd"), equilogs = TRUE)
  
