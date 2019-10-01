d<-train89
View(d)


d<-d[,c(11,12,13)]
View(d)


d1<-data.matrix(data.frame(unclass(d[,c(2,3)]))) 

View(d1)

d<-data.frame(d[1],d1)
View(d)


library(e1071)
library(caTools)

split<-sample.split(d$Loan_Status, SplitRatio = 0.7)

train<-subset(d, split==TRUE)
test<-subset(d, split==FALSE)

t<-scale(train[-3])
tt<-scale(test[-3])



classifier<-svm(formula=Loan_Status ~ .,
                data=train,
                kernel='linear',
                mehod='C-classification')


pred<-predict(classifier, newdata = tt)
pred

library(ggplot2)
plot(classifier,train)
