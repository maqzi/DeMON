#clear almost everything in memory
rm(list = ls())

library(readr)

# read data
setwd("/home/munaf/NYU_BD/individualProj/DeMON/")
fR <- read_csv(file="output/fake_reviews.csv", col_names = c("Prod_ID", "reviews"))
TimeResults <- read_csv(file="output/time_delta_scores.csv", col_names = c("Prod_ID", "TimeScore"))

mergedResults <- merge(fR,TimeResults,by.x='Prod_ID',by.y = 'Prod_ID')
merged_df = data.frame(id=mergedResults[,1], reviews =mergedResults[,2], timeScore = mergedResults[,3],stringsAsFactors=FALSE)
merged_df <- merged_df[order(merged_df$timeScore),]

## 346 PRODUCTS NEXT TO THEIR TIMESCORES. NOTHING EVIDENT FROM THIS SCRIPT YET