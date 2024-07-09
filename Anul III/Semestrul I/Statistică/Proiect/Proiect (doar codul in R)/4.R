t=mtcars
t
attach(mtcars)
#calculam media
apply(mtcars,2,mean)

#suma
apply(mtcars,1,sum)

#cuantilele
apply(mtcars,2,quantile,probs=c(0,0.25,0.50,0.75,1),na.rm=TRUE)

#histograma
par(mfrow=c(1,3))
hist(mtcars$wt,main="Weight",xlab="Weight(in 1000)",col="yellow")
hist(mtcars$mpg,main="MPG",xlab="Miles per Gallon",col="magenta")
plot(mtcars$wt, mtcars$mpg, main="Weight vs. MPG", xlab= "Weight(in 1000)", ylab= "Miles per Gallon",col="red")

##


boxplot(mpg~cyl, 
        xlab="Cylinders", ylab="Miles/(US) gallon", 
        col=topo.colors(3))
