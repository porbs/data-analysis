import pymongo
import xml.etree.ElementTree as ET

def parseXML(file):
    tree = ET.parse(file)
    root = tree.getroot()
    result = []
    for record in root.findall('record'):
        result.append({
            'first_name': record.find('first_name').text,
            'last_name': record.find('last_name').text,
            'language': record.find('language').text,
            'email': record.find('email').text,
        })
    return result

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

data = parseXML('data/dataset.xml')
for row in data:
    collection.insert(row)
    
        
    
