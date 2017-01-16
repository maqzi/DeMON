'''''''''
FILE CONTAINS ALL METHODS USED TO SAVE DATA (OR SUPPORT SUCH A PROCESS) FROM THE ENVIRONMENT TO AN EXTERNAL SOURCE
@AUTHOR: MUNAF A QAZI
@DATE: 10/14/2016
'''''''''

'''''''''
create a dump for each review in the ../data/reviewDump/ folder according to productID. Each review is first
changed to lowercase to save pre-processing time and effort in the future.

@Params:
input: aggregatedCollection (MongoDB cursor), folderName (string)
returns: None
'''''''''

def createReviewDump(aggregatedCollection,folderName):
    import os
    for doc in aggregatedCollection.find():
        documents = []
        directory = ''
        for key, values in doc.iteritems():
            if key == '_id':
                directory = '../output/' +folderName+'/' + values
                if not os.path.exists(directory):
                    os.makedirs(directory)

            if key == "reviewText" and isinstance(values, list):
                for i in values:
                    i = i.lower()
                    documents.append(i)

            if os.path.exists(directory):
                i = 0
                for d in documents:
                    i += 1
                    with open(directory+'/'+str(i)+'.txt','w') as f:
                        f.write(d)

    print 'Review Dump Successfully created. Check: ./data/'+folderName

'''''''''
create a dump for each Date in the ./data/timeDump/ folder according to productID.


@Params:
input: aggregatedCollection (MongoDB cursor), folderName (string)
returns: None
'''''''''

def createTimeDump(aggregatedCollection,folderName):
    import os

    directory = '../output/' + folderName + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    for doc in aggregatedCollection.find():
        documents = []
        for key, values in doc.iteritems():
            if key == '_id':
                fileName = values

            if key == "unixReviewTime" and isinstance(values, list):
                for i in values:
                    documents.append(i)

        if os.path.exists(directory):
            with open(directory+'/'+fileName+'.txt','w') as f:
                for d in documents:
                    f.write(d)
                    f.write('\n')

    print 'Time Dump Successfully created. Check: '+ directory
'''''''''
Print all records in MongoDB Collection.

@Params:
input: conn (MongoDB cursor)
returns: None
'''''''''
def printAll(conn):
    conn.find({}).pretty()


'''''''''
Create CSV file on disk from a dictionary object.

@Params:
input: dict (Dictionary), fileName (string)
returns: None
'''''''''
def writeToFile(dict, fileName):
    import csv
    with open('../output/' +fileName+'.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict.items():
            writer.writerow([key, value])

