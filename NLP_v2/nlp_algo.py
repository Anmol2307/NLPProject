import nltk
from pos_list import pos_list
from neg_list import neg_list
from database import *

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from parse_stanford import *

def find_aspect(unstemmed_noun):
	lmtzr = WordNetLemmatizer()
	word = lmtzr.lemmatize(unstemmed_noun)
	if word in feature_list:
		return word
	count = 0
	for syns in processed_data:
		if word in syns:
			return feature_list[count]
		else:
			count += 1
	return "unknown feature"

def find_sentiment_type(word):
	for pos in pos_list:
		if word == pos:
			return "positive"
	for neg in neg_list:
		if word == neg:
			return "negative"
	return "unknown"

def matchAorAdvMod(commands):
	for command in commands:
		if(command[0] == "amod" or command[0] == "advmod"):
			aspect = find_aspect(command[1])
			sentiment_type = find_sentiment_type(command[2])
			print command[2] + " is " + sentiment_type + " for aspect " + aspect

commands =  parseResult()
matchAorAdvMod(commands)