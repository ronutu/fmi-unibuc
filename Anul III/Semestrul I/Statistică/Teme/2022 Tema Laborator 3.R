#Tema lab 3
#To do

#1) Creati o variabila aleatoare discreta X care ia valorile 1 2 si respectiv 3
#cu probabilitatile 1/2, 1/3 si respectiv 1/6 si calculati probabilitatile
#a) P(X<2.7)
#b) P(0.5<X<3)
#c) P(X>2|X>1)
# Generalizati solutia pentru o v.a. ce ia valori de la 1 la n(cu n fixat)
#iar probabilitatile sunt generate aleator folosind functia sample()

#atribuim valorile variabilei discrete și probabilităților
X <- c(1,2,3)
prob <- c(1/2,1/3,1/6)

#a sumăm probabilitățile pentru care X este mai mic decât 2.7
P1 <- sum(prob[X<2.7])

#b
P2 <- sum(prob[0.5<X], prob[X<3])

#c
P3 <- sum(prob[X>2|X>1])

# generalizare
n <- 10   # dăm o valoare lui n ]
p <- sample(1:100,10)   #probabilitățile generate

#nu știu mai departe

#2) Construiti doi vectori x si y cu 1000 de elemente fiecare, extrase in mod
#aleator din multimea cu numere intregi -34000:45000. Stabiliti care dintre cei
#doi vectori are mai multe elemente, luate in valoare absoluta, mai mari decat
#valoarea absoluta a elementului corespondent din celalalt vector
x <- sample(-34000:45000,1000)
y <- sample(-34000:45000,1000)


