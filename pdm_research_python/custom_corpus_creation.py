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
if not os.path.exists(path):
...    os.mkdir(path)
os.path.exists(path)
import nltk.data
path in nltk.data.path
