'''
Created on 08.12.2012

@author: rklein
'''

if __name__ == '__main__':
    pass

''' Script to create a custom corpus
see Python Text Processing with NLTK Cookbook '''

# Strg + Alt + Enter for Execution

import os, os.path
path = os.path.expanduser('~/nltk_data')
if not os.path.exists(path): os.mkdir(path)
os.path.exists(path)
import nltk.data
path in nltk.data.path
print path
''' note that this should be a path in the Git_Workspace on D:\ '''

''' load a sample wordlist '''
import nltk.data
nltk.data.load('corpora/cookbook/GL_Sequent.txt', format='raw')
'nltk\n'

from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader(path + '/corpora/cookbook/', ['GL_Sequent.txt'])
reader.words()

''' reading a tagged corpus '''
from nltk.corpus.reader import TaggedCorpusReader
reader = TaggedCorpusReader(path + '/corpora/cookbook/', r'.*\.pos')
reader.words()
reader.tagged_words()
reader.sents()
reader.tagged_sents()
reader.paras()
reader.tagged_paras()

''' different Tokenizer - works? '''
from nltk.tokenize import SpaceTokenizer
reader = TaggedCorpusReader(path + '/corpora/cookbook/', r'.*\.pos',word_tokenizer=SpaceTokenizer())
reader.words()

''' different Sentence Tokenizer '''
from nltk.tokenize import LineTokenizer
reader = TaggedCorpusReader(path + '/corpora/cookbook/', r'.*\.pos', sent_tokenizer=LineTokenizer())
reader.sents()

''' chunked Corpus Reader '''
from nltk.corpus.reader import ChunkedCorpusReader
reader = ChunkedCorpusReader(path + '/corpora/cookbook/', r'.*\.chunk')
reader.chunked_words()
reader.chunked_sents()
reader.chunked_paras()

''' draw tree '''
reader.chunked_sents()[0].draw()

''' get leaves '''
reader.chunked_words()[0].leaves()
reader.chunked_sents()[0].leaves()
reader.chunked_paras()[0][0].leaves()

''' categorized corpus '''
from nltk.corpus import brown
brown.categories()

from nltk.corpus.reader import CategorizedPlaintextCorpusReader
reader = CategorizedPlaintextCorpusReader(path + '/corpora/cookbook/', r'movie_.*\.txt', cat_pattern=r'movie_(\w+)\.txt')
reader.categories()
reader.fileids(categories=['neg'])
reader.fileids(categories=['pos'])


''' using a categorized chunked corpus reader '''
import nltk.data
from catchunked import CategorizedChunkedCorpusReader
path = nltk.data.find('corpora/treebank/tagged')
reader = CategorizedChunkedCorpusReader(path, r'wsj_.*\.pos',cat_pattern=r'wsj_(.*)\.pos')
len(reader.categories()) == len(reader.fileids())
len(reader.chunked_sents(categories=['0001']))

''' Lazy corpus loader '''
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import WordListCorpusReader
reader = LazyCorpusLoader('cookbook', WordListCorpusReader,['wordlist'])
isinstance(reader, LazyCorpusLoader)
reader.fileids()
isinstance(reader, LazyCorpusLoader)
isinstance(reader, WordListCorpusReader)
