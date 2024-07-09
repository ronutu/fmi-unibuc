nrUnif = 2000
funMonteCarlo = function(x) {
  return ( (cos(50*x) + sin(20*x))^2 ) #functia de la care plecam(vrem sa o integram)
}
Sn = 0#toate observatiile
valInti = c() #integrala calculata pentru i observatii (i se afla intre 1 si n)
valInti[0] = 0
for( i in 1:nrUnif) {
  Xn = runif(1,0,1) #generez o observatie
  Sn = Sn + funMonteCarlo(Xn) #fac suma, adunand h(Xn), unde h este funtia de mai devreme
  valInti[i] = Sn/i
}
valIntMC = Sn/nrUnif #valoarea integralei
valIntMC
valR = integrate(funMonteCarlo, 0, 1)
valR
plot(valInti, type = "l", col = "red",
     xlab = "Pasul i <= n",
     ylab = "Valoarea integralei")
grid(nx = NULL, col = "lightgray", lty = "dotted",
     lwd = par("lwd"), equilogs = TRUE)
abline(h = valR[[1]], lty = "solid", col = "chartreuse4") #valoarea data de integrate()
abline(h = 0.96, lty = "dotted") #valoarea analitica
