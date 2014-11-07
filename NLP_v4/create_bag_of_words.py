# from sets import Set
from mlearn import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

min_reqd = 1
# bag_of_words = set([])
bag_of_words = {}

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

count = 0
for tuples in parsed_array:
	count += 1
	if(count == 1):
		print("0% Complete..")
	if(count == 3500):
		print("50% Complete...")
	if(count == 7000):
		print("100% Complete....")
	words = tuples[0].strip().lower().split()
	useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n','=']
	sentence = tuples[2]
	for characters in useless:
		sentence = sentence.replace(characters,"")
	sentence = sentence.strip()
	sentence = sentence.lower()
	sentence = remove_unnecessary(sentence)
	words += sentence
	for word in words:
		if word in bag_of_words.keys():
			bag_of_words[word] += 1
		else:
			bag_of_words[word] = 1

print("Accumulated The Dictionary Of Size : " + str(len(bag_of_words)))
bag_of_words_list = []
max_allowed_length = 1200
for word in bag_of_words.keys():
	if(max_allowed_length == 0):
		break
	if(bag_of_words[word] >= min_reqd):
		bag_of_words_list.append(word)
		max_allowed_length -= 1

print("Accumulated The Bag Of Words Of Size :" + str(len(bag_of_words_list)))
file_bag = open("bag_of_words.py","w")
file_bag.write("bag_of_words = "+str(bag_of_words_list))
print("Printed The Bag Of Words")		