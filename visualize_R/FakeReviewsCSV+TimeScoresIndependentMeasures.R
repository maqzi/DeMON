#clear almost everything in memory
rm(list = ls())

library(readr)

# read data
setwd("/home/munaf/NYU_BD/individualProj/DeMON/")
fR <- read_csv(file="output/fake_reviews.csv", col_names = c("Prod_ID", "reviews"))
TimeResults <- read_csv(file="output/time_delta_scores.csv", col_names = c("Prod_ID", "TimeScore"))

id <- TimeResults$Prod_ID[TimeResults$TimeScore>0.5]
score <- TimeResults$TimeScore[TimeResults$TimeScore>0.5]
df <- data.frame(id=id,score=score,stringsAsFactors = FALSE)

#USED TO GET TIMEDELTAS GREATER THAN 0.5. USING BOTH MEASURES INDEPENDENTLY IN THIS SCRIPT
# I.E. 364 FAKE REVIEWS (CS) + 98 FAKE REVIEWS (TD)
