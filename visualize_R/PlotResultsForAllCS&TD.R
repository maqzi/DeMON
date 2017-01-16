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
merged_df$cosScore[merged_df$cosScore < 0] <- 0

# plotting
x11()
ggplot(merged_df, aes(x = 1-cosScore, y = timeScore)) + geom_point(aes(color = timeScore))+
  scale_colour_continuous(guide = FALSE) +
  theme_bw() + 
  theme(                              
    axis.title.x = element_text(face="bold", color="black", size=12),
    axis.title.y = element_text(face="bold", color="black", size=12),
    plot.title = element_text(face="bold", color = "black", size=12),
    panel.grid.major.y = element_line(colour = "red", linetype = "solid")) +
  labs(x="Cosine Distance", y="Time Delta Score", title = "Plot of Average Cosine Distance vs Time Delta Scores for Electronic Reviews on Amazon")
dev.copy2pdf(file = "output/AvgCosDistVsTimeDeltaScore.pdf")
