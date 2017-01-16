'''''''''
FILE CONTAINS ALL METHODS USED TO COMPUTE COSINE SIMILARITY (OR TO SUPPORT IT)
@AUTHOR: MUNAF A QAZI
@DATE: 10/14/2016
'''''''''

import nltk
import string

'''''''''
Removes punctuation marks

@Params:
input: documents(list)
returns: (list)
'''''''''
def removePunc(documents):
    return [''.join(c for c in s if c not in string.punctuation) for s in documents]


'''''''''
Tokenizes each review, then finds stem words from the tokens and returns the matrix to the TFIDF vectorizer.
The TFIDF vector also removes all unnecessary stop words.
Note: nltk's stopword corpus could have been used as well in the following way:

#    from nltk.corpus import stopwords
#    filtered = [w for w in tokens if not w in stopwords.words('english')]

Do note, that if so, make respective changes to the TFIDF vectorizer's call.

@Params:
input: review (list)
returns: stemmed (list)
'''''''''
def tokenize(review):
    from nltk.stem.porter import PorterStemmer
    tokens = nltk.word_tokenize(review)
    stemmer = PorterStemmer()
    stemmed = stem_tokens(tokens, stemmer)
    return stemmed

'''''''''
Find stem words in each review.
Method used by tokenize(...)

@Params:
input: tokens (list), stemmer (nltk.stem.porter object)
returns: 'stemmed (list)
'''''''''
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

'''''''''
Calculate Cosine Similarity from sparse matrix for CosSim per review

@Params:
input: doc (ndarray)
returns: sim (ndarray)
'''''''''
def cosineSimilarity(doc):
    from sklearn.metrics.pairwise import cosine_similarity
    sim = cosine_similarity(doc)
    return sim

'''''''''
Calculate Average of Cosine Similarity for the entire product

@Params:
input: sim (ndarray)
returns: (float64)
'''''''''
def averageCosineSimilarity(sim):
    l = len(sim)
    s = sim.sum()
    num = (s - l)
    den = (l ** 2 - l)
    return num / den
