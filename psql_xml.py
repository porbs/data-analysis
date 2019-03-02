import psycopg2
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
user='postgres'
password='pwd'
host='localhost'

try:
    conn = psycopg2.connect("dbname={0} user={1} password={2} host={3}".format(dbname, user, password, host))
    cursor = conn.cursor()
except Exception as e:
    print(e)
    exit(-1)

data = parseXML('data/dataset.xml')
query_string = """INSERT INTO data(first_name, last_name, language, email) VALUES ('{0}', '{1}', '{2}', '{3}');"""
for row in data:
    for key, value in row.items():
        row[key] = row[key].replace("'", "''")

    query = query_string.format(row['first_name'], row['last_name'], row['language'], row['email'])
    res = cursor.execute(query)
    conn.commit()
        