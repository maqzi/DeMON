#clear almost everything in memory
rm(list = ls())

library(readr)

# read data
setwd("/home/munaf/NYU_BD/individualProj/DeMON/")
TimeResults <- read_csv(file="output/time_delta_scores.csv", col_names = c("Prod_ID", "TimeScore"))
CSResults <- read_csv(file="output/cosine_sim_scores.csv", col_names = c("Prod_ID", "CosScore"))
metaData <- read_csv(file="output/metaDATA.csv", col_names = c("asin", "description","categories","title"))

mergedResults <- merge(CSResults,TimeResults,by.x='Prod_ID',by.y = 'Prod_ID')
mergedResults <- merge(mergedResults,metaData,by.x='Prod_ID',by.y = 'asin')

some_txt = mergedResults[,5]
some_txt = gsub("u[[:digit:]][[:digit:]][[:digit:]][[:digit:]]", "", some_txt)
some_txt = gsub("[[:punct:]]", " ", some_txt)
some_txt = gsub("Electronics", "", some_txt)
some_txt = gsub("Products", "", some_txt)
some_txt = gsub("[[:space:]]+", " ", some_txt)
some_txt = trimws(some_txt)

merged_df = data.frame(id=mergedResults[,1],title = mergedResults[,6], cosScore =mergedResults[,2], timeScore = mergedResults[,3],categories = some_txt,stringsAsFactors=FALSE)

## contains all 63k products with there metadata and Time+Cos scores
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
fake_df = data.frame(id=fakeId,fakenessScore=fakeScore, stringsAsFactors=FALSE)

## FAKE_DF CONTAINS 46 PRODUCTS AFTER WEIGHTS APPLIED

categoriesVector <- c('\\<Accessories\\>','\\<Wearable\\>','\\<Computer\\>','\\<Audio\\>','\\<Speakers\\>','\\<TV\\>','\\<Musical\\>','\\<Cell Phones\\>','\\<Games\\>','\\<Headphones\\>','\\<Camera\\>','\\<Office\\>','\\<Car\\>')
fake_df_with_meta <- merge(fake_df,merged_df,by.x='id',by.y = 'id')
fake_df_with_meta$MainCategory[grepl(categoriesVector[1],fake_df_with_meta[,6])]<-'Accessories'
fake_df_with_meta$MainCategory[grepl(categoriesVector[2],fake_df_with_meta[,6])]<-'Wearable'
fake_df_with_meta$MainCategory[grepl(categoriesVector[3],fake_df_with_meta[,6])]<-'Computer'
fake_df_with_meta$MainCategory[grepl(categoriesVector[4],fake_df_with_meta[,6])]<-'Audio'
fake_df_with_meta$MainCategory[grepl(categoriesVector[5],fake_df_with_meta[,6])]<-'Speakers'
fake_df_with_meta$MainCategory[grepl(categoriesVector[6],fake_df_with_meta[,6])]<-'TV'
fake_df_with_meta$MainCategory[grepl(categoriesVector[7],fake_df_with_meta[,6])]<-'Musical'
fake_df_with_meta$MainCategory[grepl(categoriesVector[8],fake_df_with_meta[,6])]<-'Cell Phones'
fake_df_with_meta$MainCategory[grepl(categoriesVector[9],fake_df_with_meta[,6])]<-'Games'
fake_df_with_meta$MainCategory[grepl(categoriesVector[10],fake_df_with_meta[,6])]<-'Headphones'
fake_df_with_meta$MainCategory[grepl(categoriesVector[11],fake_df_with_meta[,6])]<-'Camera'
fake_df_with_meta$MainCategory[grepl(categoriesVector[12],fake_df_with_meta[,6])]<-'Office'
fake_df_with_meta$MainCategory[grepl(categoriesVector[13],fake_df_with_meta[,6])]<-'Car'

View(fake_df_with_meta)

library(ggplot2)
# plotting
x11()
Category = fake_df_with_meta$MainCategory
ggplot(fake_df_with_meta, aes(x=fake_df_with_meta$MainCategory)) +
  geom_bar(aes(y=..count.., fill=Category)) +
  scale_fill_brewer(palette="RdGy") +
  labs(x="Products", y="Number of Products") +
  labs(title = "Products with Fake Reviews")
dev.copy2pdf(file = "output/barGraph.pdf")