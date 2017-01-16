#clear almost everything in memory
rm(list = ls())

library(readr)

# read data
setwd("/home/munaf/NYU_BD/individualProj/DeMON/")
fR <- read_csv(file="output/fake_reviews.csv", col_names = c("Prod_ID", "reviews"))
TimeResults <- read_csv(file="output/time_delta_scores.csv", col_names = c("Prod_ID", "TimeScore"))
CSResults <- read_csv(file="output/cosine_sim_scores.csv", col_names = c("Prod_ID", "CosScore"))
metaData <- read_csv(file="output/metaDATA.csv", col_names = c("asin", "description","categories","title"))

mergedResults <- merge(CSResults,TimeResults,by.x='Prod_ID',by.y = 'Prod_ID')
mergedResults <- merge(mergedResults,metaData,by.x='Prod_ID',by.y = 'asin')

some_txt = mergedResults[,5]
some_txt = gsub("[[:punct:]]", "", some_txt)
some_txt = gsub("u[[:digit:]][[:digit:]][[:digit:]][[:digit:]]", "", some_txt)
some_txt = gsub("Electronics", "", some_txt)
some_txt = gsub("[ \t]{2,}", " ", some_txt)
some_txt = gsub("Accessories", "", some_txt)
some_txt = gsub("Products", "", some_txt)

merged_df = data.frame(id=mergedResults[,1],title = mergedResults[,6], cosScore =mergedResults[,2], timeScore = mergedResults[,3],categories = some_txt,stringsAsFactors=FALSE)

## contains all 63k products with there metadata and Time+Cos scores