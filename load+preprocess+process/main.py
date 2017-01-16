'''''''''
MAIN FILE FOR PROJECT
@AUTHOR: MUNAF A QAZI
@DATE: 11/03/2016
'''''''''

'''''''''
NOTES:
- Please make sure MongoServer is running.
- Please make sure all required packages have been pip installed. (Requirements.txt present).
- Please ensure nltk.download() is uncommented in the first run and the punkt corpus is downloaded.
'''''''''
from loading import *
from unloadingResults import *
from DateAnalysis import *
from CosineSimAnalysis import *
from pymongo import MongoClient

#GLOBAL VARIABLES
client = MongoClient('mongodb://localhost:27017/')
db = client['individ_DeMON4']
collectionName = 'products'

# Running Conditions
# success=True
# reviewAggregatedCollection = 'reviewsByProdID'
# timeAggregatedCollection = 'timesByProdID'

if __name__ == "__main__":
#    import nltk        #Uncomment during the first run and download the PunkT Corpus
#    nltk.download()    #Uncomment during the first run and download the PunkT Corpus
    success = readJSON('../data/Electronics_5.json',db[collectionName])
    if success == True:
        pipeline = [{"$group": {"_id": "$asin", "reviewText": {"$push": "$reviewText"}}},{"$out":"reviewsByProdID"}]
        reviewAggregatedCollection = aggregation(pipeline,db[collectionName],'reviewsByProdID')
        print('aggregated all reviews into '+str(db[reviewAggregatedCollection].find().count())+' products')
        CosSimAnalysis(db[reviewAggregatedCollection])
        createReviewDump(db[reviewAggregatedCollection],'reviewDump')

        pipeline = [{"$group": {"_id": "$asin", "unixReviewTime": {"$push": "$unixReviewTime"}}}, {"$out": "timesByProdID"}]
        timeAggregatedCollection = aggregation(pipeline,db[collectionName],'timesByProdID')
        print('aggregated all review times for ' + str(db[timeAggregatedCollection].find().count()) + ' products')
        DateTimeAnalysis(db[timeAggregatedCollection])
        createTimeDump(db[timeAggregatedCollection],'timeDump')

   # createTFIDF('./data/reviewDump/')
   # cosmatrix = readCSVFromFile()
   # finalCosine(cosmatrix)
    else:
        print "Exception Caught: Please Check JSON"
