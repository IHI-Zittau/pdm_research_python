'''
Created on 09.10.2011

@author: rklein
'''

from __future__ import division
import nltk, re, pprint

if __name__ == '__main__':
    pass

''' Set Directory '''
''' Product Manager '''
''' Craigslist '''
directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Craigslist" 
''' Monster '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-US/_Advertising-PR-Services" '''
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
''' SimplyHired '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-US/fcz-1" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-US/fcz-2" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-US/fcz-3" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-US/fcz-4" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-US/fcz-5" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-US/fcz-6" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-US/_Unknown" '''

''' AU '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-AU" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-AU" '''

''' CA '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-CA" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-CA" '''

''' UK '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/SimplyHired/SimplyHired-UK" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Manager/Monster/Monster-UK" '''

''' Any Job '''
''' directory = "C:/Programme/screen-scraper basic edition/_Any_Job/Monster/Monster-US" '''
''' directory = "C:/Programme/screen-scraper basic edition/_Any_Job/SimplyHired/SimplyHired-US" '''

''' Account Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Account_Manager/" '''

''' Application Engineer '''
''' directory = "C:/Programme/screen-scraper basic edition/_Application_Engineer/" '''

''' Brand Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Brand_Manager/" '''

''' Business Analyst '''
''' directory = "C:/Programme/screen-scraper basic edition/_Business_Analyst/" '''

''' Developer '''
''' directory = "C:/Programme/screen-scraper basic edition/_Developer/" '''

''' Innovation Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Innovation_Manager/SimplyHired/SimplyHired-US" '''

''' Marketing Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Marketing_Manager/" '''

''' Product Marketing Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Marketing_Manager/" '''

''' Product Specialist '''
''' directory = "C:/Programme/screen-scraper basic edition/_Product_Specialist/" '''

''' Program Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Program_Manager/" '''

''' Project Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Project_Manager/" '''

''' Sales Manager '''
''' directory = "C:/Programme/screen-scraper basic edition/_Sales_Manager/" '''

''' Software Engineer '''
''' directory = "C:/Programme/screen-scraper basic edition/_Software_Engineer/" '''

from nltk.corpus import PlaintextCorpusReader
files = PlaintextCorpusReader (directory, '.*')
''' files.fileids()[1:20] '''
''' files.words()[1:50] '''
''' files.sents()[5:10] '''

''' Raw Text '''
html = files.raw()
raw = nltk.clean_html(html)

''' Sentences - Cleaned from HTML'''
sentences = nltk.sent_tokenize(raw)
sentences[1:100]

''' Words '''
words = nltk.word_tokenize(raw)

type(words)
len(words)
words[:10]

text = nltk.Text(words)
type(text)
text[1020:1060]
text.collocations()
text.concordance('Product')

''' Detecting Similar Documents '''
''' Jaccard Similarity '''
def jaccard_similarity(doc1, doc2):
    a = set(doc1.split())
    b = set(doc2.split())
    similarity = float(len(a.intersection(b))*1.0/len(a.union(b))) #similarity belongs to [0,1] 1 means its exact replica.
    return similarity

doc1 = 'akroncanton/2386893277.htm'
doc2 = 'akroncanton/2489357141.htm'
jaccard_similarity(doc1, doc2)

''' help(sets) '''

''' 5.1. Using a Tagger '''
''' Find words used in the same context '''
text.similar('product')
text.similar('market')
text.similar('price')

nltk.pos_tag(text)
nltk.pos_tag(nltk.word_tokenize(sentences[10]))
nltk.UnigramTagger(nltk.word_tokenize(sentences[1:10]))