'''''''''
FILE CONTAINS SCRIPT FOR SOME MAJOR FUNCTIONS IN THEIR RAW FORM WHICH WERE THEN INCORPORATED IN VARIOUS OTHER FILES
@AUTHOR: MUNAF A QAZI
@DATE: 11/3/2016
'''''''''


from sklearn.feature_extraction.text import TfidfVectorizer
import os
import string
import nltk
from nltk.stem.porter import PorterStemmer


# Create TFIDF from reviewDump
def createTFIDF(directory):
    token_dict = {}
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            file_path = subdir + os.path.sep + file
            shakes = open(file_path, 'r')
            text = shakes.read()
            lowers = text.lower()
            no_punctuation = lowers.translate(None, string.punctuation)
            token_dict[file] = no_punctuation

    # this can take some time
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')

    tfs = tfidf.fit_transform(token_dict.values())

#Check
def finalCosine(cosmatrix):
    for singleReview in cosmatrix:
        finalvec = map(int, cosmatrix[singleReview])
        sum = 0
        for i in finalvec:
            for j in finalvec:
                print i, j

def tokenize(review):
    tokens = nltk.word_tokenize(review)
    stemmer = PorterStemmer()
    stemmed = stem_tokens(tokens, stemmer)
    return stemmed

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed