n <- 100000

valRepLogistica <- function(nr, miu, beta) {
  
  U <- runif(nr)                                     #10000 de observatii dintr-o uniforma
  return (miu-beta*log(1-U)+beta*log(U))             #inversa functiei de repartitie
}
test1 <- valRepLogistica(n, 0, 1)
test2 <- rlogis(n)

par(mfrow=c(1,2)) #afisam 2 grafice pe o linie

hist(test1,
     main="Observatii folosind metoda transformarii inverse",
     xlab="Valori obtinute",
     ylab="Nr. de aparitii",
     xlim=c(-10, 10),
     cex.main=0.7,
     col="blue")
hist(test2,
     main="Observatii folosind rlogis",
     xlab="Valori obtinute",
     ylab="Nr. de aparitii",
     xlim=c(-10, 10),
     cex.main=0.7,
     col="red")
