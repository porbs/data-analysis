import psycopg2
import csv

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

with open('data/dataset.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    csv_reader.__next__()

    query_string = """
    INSERT INTO data(first_name, last_name, language, email) VALUES ('{0}', '{1}', '{2}', '{3}');"""
    for row in csv_reader:
        for i in range(len(row)):
            row[i] = row[i].replace("'", "''")
        query = query_string.format(*row)
        res = cursor.execute(query)
        conn.commit()
    
        
    
