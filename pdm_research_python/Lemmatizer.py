'''
Created on 23.11.2012

@author: rklein
'''

if __name__ == '__main__':
    pass

''' 
Script to read text files lemmatize the content and write back to text files.
'''

# Strg + Alt + Enter for Execution

if __name__ == '__main__':
    pass

import nltk
from datetime import date

# Date Stuff for File Output
d=date.today()
run_date = d.isoformat()


''' Lemmatize the Glossaries '''
''' Directory and File Stuff '''
import os
directory = "D:/Eigene Dateien_rklein/z_Forschung/_Konferenzen/_79_ICFCA - Dresden - Concept Analysis/_Glossaries/"

#os.chdir(directory)
#os.listdir('.')
os.listdir(directory)
print os.listdir(directory)[0]

def isMp3(s):
    if s.find("GL") == -1:
        return False
    else:
        return True

list_dir = os.listdir(directory)
#print list_dir
files = filter(isMp3,list_dir)
print files

for item in files:
    print item

''' Creating and Checking out a Corpus Reader ''' 
from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader(directory, files)
reader.words()
reader.words('GL_Blackblot.txt')
reader.fileids()
reader.raw()
for element in files:
    print element
#    reader.fileids(element)
    print len(reader.words(element))

''' Lemmatizing '''
#porter = nltk.PorterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# creating tokens from terms
#terms = [nltk.word_tokenize(element) for element in reader.words('GL_Blackblot.txt')]
#print terms
#print terms[0]
#print terms[0][0]

# stemming   
#print directory
term = ""
for file_inout in files:
    input_file = directory + file_inout
    print file_inout
    terms = [nltk.word_tokenize(element) for element in reader.words(file_inout)]
    output = str(input_file.replace(".txt","_LM.txt"))
    jfile = open(output,"w")
#    print output
    for tokens in terms:
#        print tokens
        tokens = [''.join(e for e in element if e.isalpha()) for element in tokens]
        tokens = [element.lower() for element in tokens]
#        stems = [porter.stem(element) for element in tokens]
        tokens = [lemmatizer.lemmatize(element) for element in tokens]
        tokens = [element for element in tokens if len(element)>1]
        tokens = [element for element in tokens if element <> '']
#        print str(element) + ": " + str(stems)
        # output = directory + "GL_Blackblot_SM.txt"
#        print output
        jfile = open(output,'a')
        for element in tokens:
            term = term + element + " "
        term = term.rstrip()
        jfile.write(term)
        term = ""
#        [jfile.write(element + " ") for element in tokens]
        jfile.write('\n')

jfile.close()


''' Lemmatize the Sample Job Postings '''
directory = "D:/Eigene Dateien_rklein/z_Forschung/_Konferenzen/_79_ICFCA - Dresden - Concept Analysis/Data/Input/"
file_inout = "_Product_Management_2012-11-18.txt"
input_file = directory + file_inout
reader = WordListCorpusReader(directory, file_inout)
terms = [nltk.word_tokenize(element) for element in reader.words(file_inout)]
output = str(input_file.replace(".txt","_LM.txt"))
print output
jfile = open(output,"w")
for tokens in terms:
    print tokens
    tokens = [''.join(e for e in element if e.isalpha()) for element in tokens]
    tokens = [element.lower() for element in tokens]
    tokens = [lemmatizer.lemmatize(element) for element in tokens]
    tokens = [element for element in tokens if len(element)>1]
    tokens = [element for element in tokens if element <> '']
    jfile = open(output,'a')
    [jfile.write(element + " ") for element in tokens]
    jfile.write('\n')

jfile.close()

''' Testing Ground for Stemming versus Lemmatizing'''
    
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()    
terms = tokenizer.tokenize('Stemming is funnier than a bummer says the sushi loving computer scientist')
terms = tokenizer.tokenize('better walking automobile indices ')
print terms

#stems = [porter.stem(element) for element in terms]
#print stems

lemmas = [lemmatizer.lemmatize(element) for element in terms]
print lemmas