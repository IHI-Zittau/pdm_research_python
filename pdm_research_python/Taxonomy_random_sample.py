'''
Created on 18.11.2012

@author: rklein
'''

''' 
Script to take sentences from a random sample of job postings and put them into a text file.
'''

# Strg + Alt + Enter for Execution

if __name__ == '__main__':
    pass

import MySQLdb as mdb
# import sys
import nltk
# import array
import random

# import time
from datetime import date

# Date Stuff for File Output
d=date.today()
run_date = d.isoformat()

# Directory and File Stuff
import os
directory = "D:/Eigene Dateien_rklein/z_Forschung/_Publications/_Articles/_XXX/Data/Output/"

#os.listdir('.')
os.chdir(directory)
#os.listdir('.')
#output = directory + "output_RnD_" + run_date + ".txt"
stats = directory + "stats_RnD_" + run_date + ".txt"
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
        print row[1]

## Just like last summer (words in job postings)
# Get Job Titles and write to a dictionary
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM jobtype")
    numrows_types = int(cur.rowcount)
    jobtypes = {}
    jobtype_list=[]
    for i in range(numrows_types):     
        row = cur.fetchone()    
#        print row[0]
        jobtypes[str(row[0])]=row[1]
        # clumsy, but what the heck?
        jobtype_list.append(row[1])
        # create files and open them
        output = directory + jobtypes[str(row[0])] + "_" + run_date + ".txt"
#        print output
        jfile = open(output,"w")
        
#        print row
#        print str(row[0])
#        print jobtypes[str(row[0])]

# Get Job Offer IDs and write to a dictionary
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM saetze3_aussortiert2 JOIN joboffer WHERE saetze3_aussortiert2.jobofferid = joboffer.jobofferid AND saetze3_aussortiert2.`jobtypeid` = 12 AND joboffer.`anzahl_ausgewaehlter_saetze` > 2;")
    numrows_offers = int(cur.rowcount)
#    print numrows_offers
    joboffers = []
    sample_offers = []
    last = 666
    for i in range(numrows_offers):     
        row = cur.fetchone()    
        if last<>row[8]:
            last = row[8]
            joboffers.append(last)
#    print joboffers
#    for i in range(len(joboffers)):
#        print i
#        print joboffers[i]
    ''' Prepare Sample '''
    sample_range = list(xrange(len(joboffers)))    # sample of joboffers
#    print sample_range
    sample_index = random.sample(sample_range,2000)    # select sample size
#    print sample_index
    for i in range(len(sample_index)):
        sample_offers.append(joboffers[sample_index[i]])
    print sample_offers

# Get Sentences, clean, and write to text file for R
with con:
    cur = con.cursor()
#    cur.execute("SELECT * FROM saetze2_aussortiert3 JOIN joboffer WHERE saetze2_aussortiert3.jobofferid = joboffer.jobofferid AND saetze2_aussortiert3.`r_and_d` = 0 AND joboffer.`anzahl_ausgewaehlter_saetze` > 6 AND joboffer.`anzahl_ausgewaehlter_saetze` < 15")
#    cur.execute("SELECT * FROM saetze3_aussortiert2 JOIN joboffer WHERE saetze3_aussortiert2.jobofferid = joboffer.jobofferid AND saetze3_aussortiert2.`jobtypeid` = 12 AND joboffer.`anzahl_ausgewaehlter_saetze` > 2")
    cur.execute("SELECT * FROM saetze3_aussortiert2 JOIN joboffer WHERE saetze3_aussortiert2.jobofferid = joboffer.jobofferid AND saetze3_aussortiert2.`jobtypeid` = 12 AND joboffer.`anzahl_ausgewaehlter_saetze` > 2;")
    numrows = int(cur.rowcount)
    last = 666
    FIRST = True
    jcount = 1 # job count
    scount = 0 # sentence count
    job = []
    print sample_index
    print sample_offers
    for i in range(numrows):
        row_p = row             # previous row
        row = cur.fetchone() 
        tokens = nltk.word_tokenize(row[1])
        ## pre-processing
        # remove punctuation & numbers
        tokens = [''.join(e for e in element if e.isalpha()) for element in tokens]
        # lowercase
        tokens = [element.lower() for element in tokens]
        # remove empty 
        tokens = [element for element in tokens if element <> '']
        # remove single characters
        tokens = [element for element in tokens if len(element)>1]
        # put sentences back together as job postings with CRLF at the end        
        # jobofferid = last one
#        print row
        print row[8], last
        if row[8] == last:  
            [job.append(element) for element in tokens]
            scount = scount + 1
        elif FIRST:  
            [job.append(element) for element in tokens]
            FIRST = False
            last = row[8] 
            scount = scount + 1
        else:
            # append job to .txt file
            # kick out any jobs, which have unusually many sentences
            if (scount < 41) and (last in sample_offers):
                output = directory + jobtypes[str(row_p[7])] + "_" + run_date + ".txt"
                print output
                jfile = open(output,'a')
                print job
#                jfile.write(str(last) + "\n")
                [jfile.write(element + " ") for element in job]
                jfile.write("\n")     
                print "j: " + str(jcount)
                print "s: " + str(scount)                   
            last = row[8]    
            job=[]
#            job.append(str(row[8]))
            [job.append(element) for element in tokens]
            jcount = jcount + 1
            scount = 1

# Close all files
for i in range(len(jobtype_list)):     
    output = directory + jobtype_list[i] + "_" + run_date + ".txt"
#    print output
    jfile = open(output)
    jfile.close()          
# sfile.close()

### All Job Posting Files written and closed