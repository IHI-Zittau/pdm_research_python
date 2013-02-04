'''
Created on 09.12.2012

@author: rklein
'''

if __name__ == '__main__':
    pass

''' Script to tag text files and write them to an output directory '''

import os
directory = "D:/Eigene Dateien_rklein/z_Forschung/_Konferenzen/_79_ICFCA - Dresden - Concept Analysis/Data/"
input_directory = directory + "Input/_Product_Management/"
output_directory = directory + "1_POS/"
if not os.path.exists(output_directory): os.mkdir(output_directory)

# reading stuff
file_list = os.listdir(input_directory)
print file_list

# just for testing create a corpus reader
from nltk.corpus.reader import PlaintextCorpusReader
reader = PlaintextCorpusReader(input_directory,'.*.txt')

reader.fileids()
reader.raw()
reader.sents()
reader.words()

## default POS tagger from NLTK ##
import nltk
# import pprint
# sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
pos = "nltk"
path = output_directory + pos
if not os.path.exists(path): os.mkdir(path)
for i in range(len(file_list)):
#    posting = []
    output = path + "/" + str(file_list[i])
    jfile=open (output,"w")
    reader = PlaintextCorpusReader(input_directory,str(file_list[i]))
    text = str(reader.raw())
    sents = nltk.sent_tokenize(text)
#    print sents
    for sent in sents:
        sentence = []
        tokens = nltk.word_tokenize(sent)
#        print tokens
        text_pos = nltk.pos_tag(tokens)
#        print " ".join(word+"/"+tag for word, tag in text_pos)
        jfile.write(str(" ".join(word+"/"+tag for word, tag in text_pos)))
        jfile.write("\n")
    jfile.close()
                            
## TreeTagger from Helmut Schmid using the Wrapper from Laurent Pointal ##
from TreeTaggerWrapper import treetaggerwrapper
#1) build a TreeTagger wrapper:
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='D:/Programme/TreeTagger')
#2) tag your text.
tags = tagger.TagText("This is a very short text to tag.")
#3) use the tags list... (list of string output from TreeTagger).
print tags

   
# Check, whether the format of the tagged postings is good for the tagged corpus reader
# p.51 NLTK Cookbook
input_directory = path
from nltk.corpus.reader import TaggedCorpusReader
reader = TaggedCorpusReader(input_directory, r'.*\.txt')
reader.words()
# ['The', 'expense', 'and', 'time', 'involved', 'are', ...]
reader.tagged_words()
reader.sents()
reader.tagged_sents()
reader.paras()
reader.tagged_paras()

# testing the import #
#import sys
import myMath

print myMath.add(4,5)
print myMath.division(4, 2)
print myMath.multiply(10, 5)
print myMath.fibonacci(8)
print myMath.squareroot(48)