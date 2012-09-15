'''
Created on 14.09.2012

@author: rklein
'''

if __name__ == '__main__':
    pass

# start MongoDB from command line
# mongod --logpath D:/MongoDB/mongo.logfile --port 27017 --dbpath D:/MongoDB/Data

# if the MYSQL DB doesn't contain the latest data, get it in .sql format from Peter and import
# $ mysql -u Python -p Python -h localhost harlandsql7 < joboffer3.sql 

# export joboffer3 to .csv (UTF-8) with a header line
# import into MongoDB using the below script from the cmd shell, not Mongo (superfast), INSTEAD of dealing with Python !!!
# mongoimport -d jobs -c joboffer3 -type csv --headerline --drop D:/MongoDB/Data/joboffer3.csv


# setup MongoDB connection
import pymongo
connection = pymongo.Connection("localhost", 27017)
db = connection.jobs
db.name

db.joboffer3.find_one()

# setup MySQL connection
import MySQLdb as mdb
con = mdb.connect('localhost', 'Python','Python', 'harlandsql7');
# test database access
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM saetze3_aussortiert")
    numrows = int(cur.rowcount)
#    for i in range(numrows):
    for i in range(0,100):
        row = cur.fetchone()
        print row[1]
