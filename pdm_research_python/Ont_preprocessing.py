'''
Created on 22.07.2012

@author: rklein
'''

# Strg + Alt + Enter for Execution

if __name__ == '__main__':
    pass

import MySQLdb as mdb
# import sys
import nltk

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

# Get Sentences, clean, and write to text file for R
with con:
    cur = con.cursor()
#    cur.execute("SELECT * FROM saetze2_aussortiert3 JOIN joboffer WHERE saetze2_aussortiert3.jobofferid = joboffer.jobofferid AND saetze2_aussortiert3.`r_and_d` = 0 AND joboffer.`anzahl_ausgewaehlter_saetze` > 6 AND joboffer.`anzahl_ausgewaehlter_saetze` < 15")
#    cur.execute("SELECT * FROM saetze3_aussortiert2 JOIN joboffer WHERE saetze3_aussortiert2.jobofferid = joboffer.jobofferid AND saetze3_aussortiert2.`jobtypeid` = 12 AND joboffer.`anzahl_ausgewaehlter_saetze` > 2")
    cur.execute("SELECT * FROM saetze3_aussortiert2 JOIN joboffer WHERE saetze3_aussortiert2.jobofferid = joboffer.jobofferid AND saetze3_aussortiert2.`jobtypeid` = 12 AND joboffer.`anzahl_ausgewaehlter_saetze` > 2 LIMIT 100;")
    numrows = int(cur.rowcount)
#    print cur.fetchone()
#    row = cur.fetchone()
#    last = row[6]
    last = 666
    FIRST = True
    jcount = 1 # job count
    scount = 0 # sentence count
    job = []
    from nltk.corpus import stopwords
    english_stops = set(stopwords.words('english'))
    porter = nltk.PorterStemmer()
#    lancaster = nltk.LancasterStemmer()
#    from nltk.stem import WordNetLemmatizer
#    lemmatizer = WordNetLemmatizer()
#    sfile = open(stats,"w")
    for i in range(numrows):
#        print i
        row_p = row             # previous row
        row = cur.fetchone()      
        tokens = nltk.word_tokenize(row[1])
        print tokens
        ## pre-processing
        # remove punctuation & numbers
        tokens = [''.join(e for e in element if e.isalpha()) for element in tokens]
        # stopword removal
#        tokens = [element for element in tokens if element not in english_stops]
        # lowercase
        tokens = [element.lower() for element in tokens]
        # stemming        
#        tokens = [porter.stem(element) for element in tokens]
        # lemmatizing
#        tokens = [lemmatizer.lemmatize(element) for element in tokens]
        # remove empty 
        tokens = [element for element in tokens if element <> '']
        # remove single characters
        tokens = [element for element in tokens if len(element)>1]
        # put sentences back together as job postings with CRLF at the end        
        # jobofferid = last one
        print row
        print row[8], last
        if row[8] == last:
#            [file.write(element + " ") for element in tokens]            
            [job.append(element) for element in tokens]
            scount = scount + 1
        elif FIRST:
#            [file.write(element + " ") for element in tokens]  
            [job.append(element) for element in tokens]
            FIRST = False
            last = row[8] 
            scount = scount + 1
        else:
            last = row[8]    
#            print job
            # append job to .txt file
            # kick out any jobs, which have unusually many sentences
            if scount < 41:
#                print directory
#                print row_p[7]
                output = directory + jobtypes[str(row_p[7])] + "_" + run_date + ".txt"
                print output
                jfile = open(output,'a')
                print job
                [jfile.write(element + " ") for element in job]
                jfile.write('\n')                        
                # output stats
#                sfile.write("type;"+jobtypes[str(row_p[5])]+ ";job ID;"+str(row_p[6]) + ";sen #;"+str(i) + ";job #;"+str(jcount) + ";# "+str(scount) + '\n')
            job=[]
            [job.append(element) for element in tokens]
#            print str(row_p[5])
#            print str(row_p[6])
#            print i
#            print "j: " + str(jcount)
#            print "s: " + str(scount)
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