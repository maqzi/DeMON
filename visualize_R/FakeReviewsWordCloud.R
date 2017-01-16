#clear almost everything in memory
rm(list = ls())

library(readr)
library(tm)
library(SnowballC)
library(wordcloud)

# read data
setwd("/home/munaf/NYU_BD/individualProj/DeMON/")
fR <- read_csv(file="output/fake_reviews.csv", col_names = c("Prod_ID", "reviews"))
#TimeResults <- read_csv(file="output/time_delta_scores.csv", col_names = c("Prod_ID", "TimeScore"))
#CSResults <- read_csv(file="output/cosine_sim_scores.csv", col_names = c("Prod_ID", "CosScore"))


corpus <- Corpus(VectorSource(fR$reviews))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, PlainTextDocument)
corpus <- tm_map(corpus, removeWords, stopwords('english'))
corpus <- tm_map(corpus, stemDocument)
wordcloud(corpus, max.words = 1000, random.order = FALSE)

# comparison word cloud
x11()
#comparison.cloud(corpus,  min.freq=2, colors = brewer.pal(nemo, "Dark2"),
#                 scale = c(5,1), random.order = FALSE, title.size = 1.5)
wordcloud(corpus, max.words = 1000, random.order = FALSE)
dev.copy2pdf(file = "output/wordcloud.pdf")
