sent <- zomato1
View(sent)

sent<-sent[, c(3,14)]
View(sent)

posWords <- c("great","improvement","love","great improvement","very good","good","right","very","excellent","brilliant","beautiful","fresh","pleasant","friendly","strong","perfect","awesome","polite","courteous")

negWords <- c("hate","bad","not good","horrible","disappointed","expensive","discomfort","congested","drawback","dull","Worst","utterly","unresponsive","poor","slow","inattentive","sadly","unhappy","insane","costly","uncomfortable","")


wordsDF<- data.frame(words = posWords, value = 1,stringsAsFactors=F)

wordsDF<- rbind(wordsDF,data.frame(words = negWords, value = -1))

wordsDF$lengths<-unlist(lapply(wordsDF$words, nchar))

wordsDF<-wordsDF[ order(-wordsDF[,3]),]

scoreSentence <- function(sentence){
  score<-0
  for(x in 1:nrow(wordsDF)){
    count<-length(grep(wordsDF[x,1],sentence))
    if(count){
      score<-score + (count * wordsDF[x,2])
      sentence<-sub(wordsDF[x,1],'',sentence)
    }
  }
  score
}


SentimentScore<-ifelse(SentimentScore=1, 'Positive', 'Negative')

SentimentScore<- unlist(lapply(sent$reviews_list, scoreSentence))

d1<-cbind(sent, SentimentScore)

View(d1)


d1$SentimentScore<-ifelse(d1$SentimentScore== -1, 'Negative', 'Positive')



View(d1)
