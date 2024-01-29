import re
import os
import sys
import pandas as pd 
import numpy as np 
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
import textblob
from textblob import TextBlob

def _get_wordcounts(x):
	length=len(str(x).split())
	return length

def _get_charcounts(x):
	s=x.splits()
	x=''.join(s)
	return len(x)

def _get_avg_wordlength(x):
	count=_get_charcounts(x)/_get_wordcounts(x)
	return count

def _get_stopwords_counts(x):
	l=len([t for t in x.split() if t in stopwords])
	return l

def _get_hashtag_counts(x):
	l=len([t for t in x.split() if t.startswith('#')])
	return l
def _get_mentions_counts(x):
	l=len([t for t in x.split() if t.startswith('@')])
	return l
def _get_digit_counts(x):
	return len([t for t in x.split() if t.isdigit()])
def _get_uppercase_counts(x):
	return len([t for t in x.split() if t.isupper()])

# def _get_cont_exp(x):
# 	contractions={

#     "u" : "you",

#     "ur" : "your",

#     " n" : "and",

#     "i'm" : "i am",

#     "he'll" : "he will",

#     "don't" : "do not"}
#     if type(x) is str:
#         for key in contractions:
#             value = contractions[key]
#             x = x.replace(key, value)
#         return x
#     else:
#         return x
 
def _remove_html_tags(x):
	return BeautifulSoup(x,'lxml').get_text().strip()

def _remove_accented_chars(x):
	x=unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
	return x


def _remove_stopwords(x):
	return ' '.join([t for t in x.split() if t not in stopwords])

def make_base(x):
	 x=str(x)
	 x_list=[]
	 doc=nlp(x)
	 for token in doc:
	 	lemma=token.lemma_
	 	x_list.append(lemma)
	 return' '.join(x_list)

# def _remove_common_words(x,n=20):
# 	text=x.split()
# 	freq_comm=pd.Series(text).value_counts()
# 	fn=frq_comm[:n]
# 	x=' '.join([t for t in x.split()if t not in f20])
#     return x


def _remove_rarewords(x,n=20):
	text=x.split()
	freq_comm=pd.Series(text).value_counts()
	fn=freq_comm.tail(n)

def _spelling_correction(x):
	x=TextBlob(x).correct()
	return x


