'''
Created on 09.12.2012

@author: rklein
'''

''' 
Script to take sentences from a random sample of job postings and put them
into text files named with the job_id.
'''

# Strg + Alt + Enter for Execution

if __name__ == '__main__':
    pass

import MySQLdb as mdb
import nltk
import random
from datetime import date

# Date Stuff for File Output
d=date.today()
run_date = d.isoformat()

# Directory and File Stuff
import os
directory = "D:/Eigene Dateien_rklein/z_Forschung/_Konferenzen/_79_ICFCA - Dresden - Concept Analysis/Data/Output/_Product_Management/"

#os.listdir('.')
os.chdir(directory)
#os.listdir('.')
#output = directory + "output_RnD_" + run_date + ".txt"
#stats = directory + "stats_RnD_" + run_date + ".txt"
#print output

con = mdb.connect('localhost', 'Python','Python', 'harlandsql7');

# test database access
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM saetze3_aussortiert2 LIMIT 100;")
    numrows = int(cur.rowcount)
    print('Testing Database Access')
    for i in range(numrows):
        row = cur.fetchone()
        print row

# Get sentences and write to respective files; assume the sentences are already clean
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM saetze3_aussortiert2 WHERE jobtypeid = 12 LIMIT 100;")
    numrows_saetze = int(cur.rowcount)
    print numrows_saetze
    for i in range(numrows_saetze):
        row = cur.fetchone()
        print row
        jobid = row[8] 
        sentence = row[1]
        output = directory + str(jobid) + ".txt"
        print output
        jfile = open(output,'a')
        jfile.write(str(sentence) + "\n")

# Close all files
file_list = os.listdir(directory)
print file_list
for i in range(len(file_list)):     
    output = directory + file_list[i]
#    print output
    jfile = open(output)
    jfile.close()  


### All Job Posting Files written and closed