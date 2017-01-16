'''''''''
FILE CONTAINS ALL METHODS USED TO LOAD DATA (OR SUPPORT SUCH A PROCESS) FROM AN EXTERNAL SOURCE TO ENVIRONMENT
@AUTHOR: MUNAF A QAZI
@DATE: 10/14/2016
'''''''''

'''''''''
Stores an input json to a Collection in MongoDB

@Params:
input: pathname (string), conn (MongoDB cursor)
returns: success (boolean)
'''''''''
def readJSON(jsonFiles, conn):
    count = 0
    success = False
    try:
        with open(jsonFiles,'r') as data_file:
            for l in data_file:
                dictData = filterKeys(l)
                conn.insert(dictData)
                count=count+1
                print count, 'records inserted into Mongo Collection'
    except ValueError:
        print('Failed: Empty JSON or bad Response ' + jsonFiles)
    else:
        print('Success: '+str(count)+' records pushed into MongoDB successfully!')
        success = True
    return success

'''''''''
Converts the UnixDateTime to DateTime and filters the JSON to return a dictionary with only required Keys.
Method used by readJSON(...)

@Params:
input: l (json object)
returns: dataDict (Dictionary)
'''''''''
def filterKeys(l):
    import json
    import time
    dataDict = json.loads(l)
    for key,value in dataDict.items():
        if key == "unixReviewTime":
            value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(value)) #Fixing Time
            dataDict[key] = value

        if key not in ["asin","reviewText","overall","unixReviewTime","summary"]: #DataFiltering
            dataDict.pop(key,None)
    return dataDict


'''''''''
Aggregates the main collection as per the pipeline and returns aggregated collection name.

For DeMON: the pipeline should be:
pipeline = [{"$group": {"_id": "$asin", "reviewText": {"$push": "$reviewText"}}},{"$out":"byProdID"}]

so as to create a new collection called byProdID which contains all reviews(key:reviewText) for each product joined by productID(key:asin).

@Params:
input: pipeline (string), conn (MongoDB cursor), collName (string)
returns: 'byProdID' (STATIC string)
'''''''''
def aggregation(pipeline,conn,collName):
    conn.aggregate(pipeline , allowDiskUse=True)
    return collName


'''''''''
Reads data from a CSV file on disk into a dictionary and returns it

fileName should include complete path from script location (DeMON>scripts), e.g. ../output/'+fileName+'.csv
@Params:
input: fileName (string)
returns: mydict (Dictionary)
'''''''''
def readCSVFromFile(fileName):
    import csv
    with open(fileName, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        mydict = dict(reader)
    return mydict
