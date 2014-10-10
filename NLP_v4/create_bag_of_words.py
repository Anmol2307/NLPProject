# from sets import Set
from mlearn import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

bag_of_words = set([])


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

for tuples in parsed_array:
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
   		bag_of_words.add(word)

file_bag = open("bag_of_words.py","w")
bag_of_words = list(bag_of_words)
file_bag.write("bag_of_words = "+str(bag_of_words))
    
