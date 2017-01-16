'''''''''
FILE CONTAINS SCRIPT TO DO A DATETIME-ANALYSIS OVER DATASET
@AUTHOR: MUNAF A QAZI
@DATE: 11/03/2016
'''''''''
from unloadingResults import *

'''''''''
This script encodes the following functionality:

1. Read the aggregated collection from MongoDB (DataSet Filtering has already taken place during loading).
2. For all review date times, calculate time deltas.
3. Analyze time deltas to evaluate if there have been any peaks in review postings.
4. Count all reviews posted with in 7 days of each other.
5. Calculate a normalized score, i.e: score (from point 4) / total number of reviews.
6. Write normalized score to a CSV.

@Params:
input: timeAggregated (MongoDB cursor)
returns: None
'''''''''
def DateTimeAnalysis(timeAggregated):
    print "Beginning DateTime Analysis"
    time_score = {}
    count = 0
    total = timeAggregated.find().count()
    for doc in timeAggregated.find():
        times = []
        for key, values in doc.iteritems():
            if key == '_id':
                prod_id = values

            if key == 'unixReviewTime' and isinstance(values,list):
                for i in values:
                    times.append(convertStringtoDate(i))

        score, diff_matrix = calculateTimeDeltas(times)
        normalized_time_score = float(score)/((len(times)**2-len(times))/2)
        time_score[prod_id] = normalized_time_score

        count += 1
        print 'processed: ' + str(count) + ' out of ' + str(total) + ' products'

    writeToFile(time_score,'time_delta_scores')
    print "Analysis Complete, results written to CSVs"

'''''''''
Calculate difference between all review times per product

@Params:
input: times (list)
returns: count (int), diff_mat (ndarray)
'''''''''
def calculateTimeDeltas(times):
    diff_mat = [[0 for w in range(len(times))] for h in range(len(times))]
    count = 0
    for x in range(0, len(times)):
        for y in range(x + 1, len(times)):
            diff_mat[x][y] = abs(times[x] - times[y])
            if diff_mat[x][y].days <= 7:
                count += 1

    return count, diff_mat

'''''''''
Convert date/time string to a datetime object.

@Params:
input: dateTimeString (string)
returns: date_object (DateTime)
'''''''''
def convertStringtoDate(dateTimeString):
    from datetime import datetime
    date_object = datetime.strptime(dateTimeString,'%Y-%m-%d %H:%M:%S')
    return date_object