from bag_of_words import *
from senti_bag_of_words import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

def remove_unnecessary(sentence):
  s1 = PunktWordTokenizer().tokenize(sentence)
  s2 = nltk.pos_tag(s1)
  useful = ["JJ","JJS","JJS","NN","NNS","NNP","NNPS","RB","RBR","RBS"]
  splitted = []
  # print s2
  lmtzr = WordNetLemmatizer()
  for pairs in s2:
    if(pairs[1] in useful):
      splitted.append(lmtzr.lemmatize(pairs[0]))
  return splitted

def create_dictionary(sentence):
	dictionary = {}
	count_dictionary = {}

	count = 1
	for word in bag_of_words:
		count_dictionary[word] = count
		dictionary[count] = 0
		count += 1
		
	useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
	# sentence = tuples[2]
	for characters in useless:
		sentence = sentence.replace(characters,"")
	sentence = sentence.strip()
	sentence = remove_unnecessary(sentence)

	for word in sentence:
		if(word in count_dictionary.keys()):
	  		dictionary[count_dictionary[word]] += 1

	return dictionary

def create_senti_dictionary(sentence):
	dictionary = {}
	count_dictionary = {}

	count = 1
	for word in senti_bag_of_words:
		count_dictionary[word] = count
		dictionary[count] = 0
		count += 1
		
	useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
	# sentence = tuples[2]
	for characters in useless:
		sentence = sentence.replace(characters,"")
	sentence = sentence.strip()
	sentence = remove_unnecessary(sentence)

	for word in sentence:
		if(word in count_dictionary.keys()):
	  		dictionary[count_dictionary[word]] += 1
	  		# print(word)

	return dictionary