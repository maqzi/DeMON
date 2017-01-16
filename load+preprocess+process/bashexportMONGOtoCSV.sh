#!/bin/sh

#export metadata from collection to csv for R
mongoexport --db individ_DeMON2 --collection metaData --type=csv --fields asin,description,categories,title --out /home/munaf/NYU_BD/individualProj/DeMON/output/metaDATA.csv

