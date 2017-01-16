#clear almost everything in memory
rm(list = ls())

library(ggplot2)
library(readr)

# read data
setwd("/home/munaf/NYU_BD/individualProj/DeMON/")
CosResults <- read_csv(file="output/cosine_sim_scores.csv", col_names = c("Prod_ID", "CosScore"))
TimeResults <- read_csv(file="output/time_delta_scores.csv", col_names = c("Prod_ID", "TimeScore"))

# create data frame
mergedResults <- merge(CosResults,TimeResults,by.x='Prod_ID',by.y = 'Prod_ID')
merged_df = data.frame(id=mergedResults[,1], cosScore =mergedResults[,2], timeScore = mergedResults[,3],stringsAsFactors=FALSE)

# sort data frame
merged_df <- merged_df[order(merged_df$cosScore, merged_df$timeScore),]

# fakeness weights
cosWeight <- 0.25
timeWeight <- 0.75
final_df <- merged_df
final_df$cosScore[final_df$cosScore < 0] <- 0
final_df$cosScore <- final_df$cosScore*cosWeight
final_df$timeScore <- final_df$timeScore*timeWeight
final_df$fakeness <- final_df$cosScore+final_df$timeScore
fakeScore <- final_df$fakeness[final_df$fakeness > 0.5]
fakeId <- final_df$id[final_df$fakeness > 0.5]
fake_df = data.frame(id=fakeId,score=fakeScore, stringsAsFactors=FALSE)

## FAKE_DF CONTAINS 46 PRODUCTS AFTER WEIGHTS APPLIED