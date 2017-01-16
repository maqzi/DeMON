#!/bin/sh

#import Cellphone Data JSON to Mongo
mongoimport --db individ_DeMON --collection cellphoneDataMain --drop --file /home/munaf/NYU_BD/individualProj/DeMON/data/Cell_Phones_and_Accessories_5.json

#import Electronics Data JSON to Mongo
mongoimport --db individ_DeMON --collection ElectronicsDataMain --drop --file /home/munaf/NYU_BD/individualProj/DeMON/data/Electronics_5.json

#import metaData to Mongo
mongoimport --db individ_DeMON --collection metaData --drop --file /home/munaf/NYU_BD/individualProj/DeMON/data/meta_Electronics.json


#Basic commands
#mongo individ_DeMON --eval "db.cellphones.findOne()"
#mongo individ_DeMON --eval "db.getCollectionNames()"
