from senti_bag_of_words import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

set_senti_bag = set([])

for word in senti_bag_of_words:
	lmtzr = WordNetLemmatizer()
	word = lmtzr.lemmatize(word)
	if(len(word) <= 8):
		set_senti_bag.add(word)

set_senti_bag = list(set_senti_bag)

file_senti = open("senti_bag_of_words.py","w")
file_senti.write("senti_bag_of_words = " + str(set_senti_bag))

