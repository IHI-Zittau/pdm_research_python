'''
Created on 16.09.2012

@author: rklein
'''

if __name__ == '__main__':
    pass

### Monster job posting import using Beautiful Soup

## Import packages
# import NLTK
from __future__ import division
import nltk

# import Beautiful Soup library
from bs4 import BeautifulSoup


## import text

''' Set Directory '''
''' Monster '''
directory = "C:/Program Files/screen-scraper basic edition/_Product_Manager/Monster/Monster-US"
# directory = "C:/Program Files/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/Accounting-Auditing-Services"
# directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Advertising-PR-Services"
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Banking" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Biotechnology-Pharmaceuticals" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Business-Services-Other" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Computer-Hardware" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Computer-IT-Services" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Computer-Software" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Consumer-Packaged-Goods-Manufacturing" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Electronics-Components-Semiconductor-Mfg" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Energy-Utilities" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Engineering-Services" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Financial-Services" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Healthcare-Services" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Insurance" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Internet-Services" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Management-Consulting-Services" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Manufacturing-Other" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Medical-Devices-Supplies" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Printing-Publishing" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Retail" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Telecommunications-Services" '''

# import textreader from NLTK
from nltk.corpus import PlaintextCorpusReader
files = PlaintextCorpusReader (directory, '.*')
files.fileids()[1:20] # works
# files.words()[1:50] - doesn't work
# files.sents()[5:10] - doesn't work

# Raw Text 
html_doc = files.raw()
print html_doc

soup = BeautifulSoup(html_doc)
print soup

''' How come only the first file content is shown? '''
soup.text               # right her
soup.title
soup.a
soup.find_all('a')
soup.find_all('text')
print(soup.get_text())  # now it shows more (the whole?)

# Sentences - Cleaned from HTML
sentences = nltk.sent_tokenize(soup.get_text)

for element in sentences:
    print element           # not very good with this type of data - needs finetuning
    