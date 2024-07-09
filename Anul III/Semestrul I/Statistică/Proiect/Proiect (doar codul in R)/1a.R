n=10000

valRepLogistica=function(nr) {
  
  u=runif(nr) #10000 de observatii dintr-o uniforma
  return (log(u/(1-u))) #inversa functiei de repartitie
}
test1=valRepLogistica(n)
test2=rlogis(n)

par(mfrow=c(1,2)) #afisam 2 grafice pe o linie

hist(test1,
     main="Observatii folosind metoda transformarii inverse",
     xlab="Valori obtinute",
     ylab="Nr. de aparitii",
     xlim=c(-10, 10),
     cex.main=0.7,
     col="blue");
hist(test2,
     main="Observatii folosind rlogis",
     xlab="Valori obtinute",
     ylab="Nr. de aparitii",
     xlim=c(-10, 10),
     cex.main=0.7,
     col="red");
