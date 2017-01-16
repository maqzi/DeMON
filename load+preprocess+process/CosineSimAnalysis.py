'''''''''
FILE CONTAINS SCRIPT TO DO A COSINE-SIMILARITY-ANALYSIS OVER DATASET
@AUTHOR: MUNAF A QAZI
@DATE: 10/30/2016
'''''''''

from CosineSimilarityCode import *
from sklearn.feature_extraction.text import TfidfVectorizer
from unloadingResults import writeToFile
'''''''''
This script encodes the following functionality:

1. Read the aggregated collection from MongoDB (DataSet Filtering has already taken place during loading).
2. Preprocess (Change to lowercase, remove all punctutation marks and tokenize).
3. Remove all stop words (as per the punkt corpus).
4. Use stems for all remaining tokens
5. Create a TFIDF vectorizer.
6. Evaluate a sparse matrix with the TFS Scores using the vectorizer.
7. Calculate Pairwise Cosine Similarity for the matrix.
8. Calculate Average Cosine Similarity of all reviews for each product.
9. Evaluate if average and pairwise cosine similarity of any review is greater than a threshold
    and classify them.
10. Write potential fake reviews, products with a majority of fake reviews,
    and average cosine score for each product in CSVs.

@Params:
input: aggregatedCollection (MongoDB cursor)
returns: None
'''''''''

def CosSimAnalysis(aggregatedCollection):
    print "Beginning CosineSimilarity Analysis"
    cos_dict = {}
    fake_dict = {}
    fake_reviews = {}
    count = 0
    total = aggregatedCollection.find().count()

    for doc in aggregatedCollection.find():
        documents = []
        for key, values in doc.iteritems():
            if key == '_id':
                prod_id = values

            if key == "reviewText" and isinstance(values,list):
                for i in values:
                    i = i.lower()
                    documents.append(i)

        no_punctuation = removePunc(documents)
        tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
        tfs = tfidf.fit_transform(no_punctuation)
        sim = cosineSimilarity(tfs)

        avgCosScore = averageCosineSimilarity(sim)
        cos_dict[prod_id] = avgCosScore

        if(avgCosScore > 0.5):
            fake_dict[prod_id] = avgCosScore

        review=0
        potential_fakes=[]
        for each_r in sim:
            column = 0
            review+=1
            for each_c in each_r:
                column+=1
                if each_c > 0.7 and review != column:
                    potential_fakes.append(documents[review-1])

        if len(potential_fakes)>0:
            fake_reviews[prod_id] = potential_fakes

        count+=1
        print 'processed: '+str(count)+' out of '+str(total)+' products'

    writeToFile(cos_dict,'cosine_sim_scores')
    writeToFile(fake_dict, 'fake_prods')
    writeToFile(fake_reviews, 'fake_reviews')
    print "Analysis Complete, results written to CSVs"
