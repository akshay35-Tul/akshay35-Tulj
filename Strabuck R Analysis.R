d<-starbucks_drinkMenu_expanded
View(d)


colnames(d2)

d3<-d2[order(-d2$Calories, na.last=NA) , ]
View(d3)

library(tidyverse)

d4<-d3%>% 
  group_by(Beverage)%>%
  summarise(average = mean(Caffee))
View(d4)


d5<-d4[order(-d4$average, na.last=NA) , ]
View(d5)


#How to take last three characters and numbers from text
substrRight <- function(d5, n){
  substr(d5, nchar(d5)-n+1, nchar(d5))
}




d6<-substrRight(d5$average, 4)
View(d6)



d7<-data.frame(d5$Beverage,d6)
View(d7)


View(d5)

#How to take first three characters or Numbers from text
substrRight <- function(d5, n){
  substr(d5, nchar(d5)-n, nchar(d5))
}

d8<-substr(d5$average, start = 1, stop = 3)
View(d8)

d9<-data.frame(d5$Beverage, d8)
View(d9)

View(d3)
d10<-d3[,c(3,4,9,10)]
View(d10)
#By for mean
by(d10[,2:4], d10$Beverage_prep, colMeans)

#Remove NA

d<-train89
View(d)

d1<-d[complete.cases(d), ]
View(d1)


d<-Train_SU63ISt
View(d)

#How to remove last three characters
d1<-substr(d$Datetime,1,nchar(d$Datetime)-5) 
View(d1)
d<-d[,c(1,3)]
d2<-data.frame(d, d1)
View(d2)

#How to remove last three characters
d8<-substr(d$Beverage_prep,1,nchar(d$Beverage_prep)-2) 
View(d8)

# Removing first and last characters.
library(stringr)
d10<-str_sub(d$Beverage_prep, 2, -3)
View(d10)

#Remove firsty three characters
d11<-substring(d$Beverage_prep, 3)
View(d11)



# Changing Numeric Variable to Categorical in R

d<-train
View(d)
d<-d[complete.cases(d), ]
View(d)

GPA1<-cut(d$`GPA Score in Graduation`, breaks = c(0,75,90,100), labels = c('C','B','A'), right = FALSE)
GPA1
GPA<-cut(d$`GPA Score in Graduation`, breaks = c(0,75,90,100), labels = c('C','B','A'), right = FALSE)
GPA


d3<-data.frame(d, GPA)
View(d3)

#Convert categorical variable into numeric
cat = c(rep("High",2),rep("Medium",1), rep("Low", 0))
catn1 = factor(cat, labels=(1:length(levels(factor(cat)))))
catn = as.numeric(catn1)

#Convert categorical variable into numeric
data.matrix(data.frame(unclass(d[,c(2,3)]))) 


#invalid argument to unary operator
#as.numeric(as.character(d$votes)) for column
d$votes <- as.numeric(as.character(d$votes))

d3<-d[order(-d$votes, na.last = NA),]
View(d3)


#'nchar()' requires a character vector
#nchar(as.character(x_fac)) 

d6<-substr(d5$d1,1,nchar(as.character(d5$d1))-6) 
View(d6)

#Descibe 
library(Hmisc)

describe(d)


#Give prediction to predict
pred$C1 <- ifelse(pred$C >= 0.5,'Yes','No')
pred$B1 <- ifelse(pred$B >=0.5 ,'Yes','No')
pred$A1 <- ifelse(pred$A >=0.5 ,'Yes','No')
pred

View(pred)


#Give prediction to predict
Result<-ifelse(pred$High >= 0.5, 'High', 'Low')
Result

pred<-data.frame(pred, Result)
View(pred)

#Replace value with another value

d$Chocklates[d$Chocklates %in% 1] <- "yes"
d$Chocklates[d$Chocklates %in% 0] <- "no"


#Association Rules only first 5

inspect(rules[1:5])