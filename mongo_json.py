import pymongo
import json

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

with open('data/dataset.json') as f:
    data = json.load(f)
    for row in data:
        collection.insert(row)
    
        
    
