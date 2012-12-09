'''
Created on 09.12.2012

@author: rklein
'''

if __name__ == '__main__':
    pass

''' Script to tag text files and write them to an output directory '''

import os
directory = "D:/Eigene Dateien_rklein/z_Forschung/_Konferenzen/_79_ICFCA - Dresden - Concept Analysis/Data/Output/_Product_Management/"

# reading stuff
file_list = os.listdir(directory)
print file_list

# just for testing create a corpus reader
from nltk.corpus.reader import PlaintextCorpusReader
reader = PlaintextCorpusReader(directory,'.*.txt')
reader.fileids()

reader.raw()
reader.words()

# tagging
import nltk

# tokenizing
import pprint
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
for i in range(len(file_list)):
    reader = PlaintextCorpusReader(directory,str(file_list[i]))
    text = str(reader.raw)
    sents = sent_tokenizer.tokenize(text)
    pprint.pprint(sents)

# default tagger from NLTK
pos = "nltk"
path = directory + pos
if not os.path.exists(path): os.mkdir(path)
for i in range(len(file_list)):
    reader = PlaintextCorpusReader(directory,str(file_list[i]))
    text_pos = nltk.pos_tag(reader.words()) # word tokenizer included
    output = path + "/" + str(file_list[i])
    jfile=open (output,"w")
    try:
        jfile.write(str(text_pos))
    finally:
        jfile.close()

