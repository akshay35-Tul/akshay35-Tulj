d<-heart
View(d)

n_index<-round(0.8*nrow(d))
n_train<-sample(1:nrow(d), n_index)
train<-d[n_train,]
test<-d[-n_train,]

model<-glm(target ~ ., data=train)
summary(model)

pred<-predict(model, test)
pred

pred<-data.frame(pred)
View(pred)

