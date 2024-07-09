n=10000

valorRepCauchy=function(nr){
  
  u=runif(nr) #10000 de observatii dintr-o uniforma
  return(tan(pi*(u-1/2))) #inversa functiei date
}

test1=valorRepCauchy(n) #observatii metoda inversei
test2=rcauchy(n,0,1) #observatii metoda rcauchy

par(mfrow=c(1,2)) #afisam 2 grafice pe o linie

hist(test1,
     main="Observatii folosind metoda transformarii inverse",
     xlab="Valori obtinute",
     ylab="Nr. de aparitii",
     cex.main=0.7,
     col="green");

hist(test2,
     main="Observatii folosing rcauchy",
     xlab="Valori obtinute",
     ylab="Nr. de aparitii",
     cex.main=0.7,
     col="orange");

