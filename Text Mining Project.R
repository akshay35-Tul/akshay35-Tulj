d<-zomato1
View(d)


library(ggplot2)
library(tm)
library(dplyr)
library(tm.plugin.webmining)
library(tidytext)
library(gutenbergr)

dickens<-d[,c(3,14)]
View(dickens)

tidy_dickens <- dickens %>%
  unnest_tokens(word, reviews_list) %>%
  anti_join(stop_words)
View(tidy_dickens)

bing_tidy_count<-tidy_dickens%>%
  inner_join(get_sentiments("bing"))%>%
  count(name, word, sentiment, sort = FALSE)%>%
  ungroup()
View(bing_tidy_count)
View(bing_tidy_count)

bing_tidy_count<-bing_tidy_count[,-3]
View(bing_tidy_count)
bing_tidy_count<-table(bing_tidy_count)
View(bing_tidy_count)



