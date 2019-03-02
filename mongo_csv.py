import pymongo
import csv

dbname='lab1'
collection='data'
user='root'
password='pwd'
host='localhost'
port=27017
uri = "mongodb://{0}:{1}@{2}:{3}/{4}?authSource=admin".format(user, password, host, port, dbname)
try:
    client = pymongo.MongoClient(uri)
    db = client[dbname]
    collection = db[collection]
except Exception as e:
    print(e)
    exit(-1)

with open('data/dataset.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    csv_reader.__next__()

    for row in csv_reader:
        print(row)
        collection.insert({
            "first_name": row[0],
            "last_name": row[1],
            "language": row[2],
            "email": row[3]
        })
    
        
    
