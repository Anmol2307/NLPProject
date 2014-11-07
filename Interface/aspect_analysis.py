import math

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

import sys
sys.path.insert(0, '../NLP_V3')
from database import *
from trained_model import *

file_out_text = open("testresult_header.py",'w')
result_header_map = {}

def remove_unnecessary(sentence):
	s1 = PunktWordTokenizer().tokenize(sentence)
	s2 = nltk.pos_tag(s1)
	useful = ["JJ","JJS","JJS","NN","NNS","NNP","NNPS","RB","RBR","RBS"]
	splitted = []
	# print s2
	for pairs in s2:
		if(pairs[1] in useful):
			splitted.append(pairs[0])
	return splitted

def get_non_nouns(sentence):
	s1 = PunktWordTokenizer().tokenize(sentence)
	s2 = nltk.pos_tag(s1)
	useful = ["JJ","JJS","JJS","RB","RBR","RBS"]
	splitted = []
	# print s2
	for pairs in s2:
		if(pairs[1] in useful):
			splitted.append(pairs[0])
	return splitted


def compute_for_aspect(aspect,sentence,ad_words):
	score = 0
	probability = 0
	count = 0
	for word in sentence:
		phrase = aspect + "|" + word
		if(phrase in probability_aspect_given_word.keys()):
			probability += probability_aspect_given_word[phrase]
			if(word in ad_words):
				score += score_aspect_and_word[phrase]
				count += 1
	# print(probability)
	if(count != 0):
		return [probability,(1.0*score)/(1.0*count)]
	else:
		return [probability,0]

feature_word_map = {}
score_map = {}

def understand_sentence(sentence,count):
	useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
	for characters in useless:
		sentence = sentence.replace(characters,"")
	sentence = sentence.strip()
	sentence = sentence.lower()
	print(count)
	print(sentence)
	rel_words = remove_unnecessary(sentence)
	ad_words = get_non_nouns(sentence)
	
	
	sentence = sentence.split()
	lmtzr = WordNetLemmatizer()
	for word in sentence:
		word = lmtzr.lemmatize(word)
	power = {}

	for aspect in feature_list:
		power[aspect] = compute_for_aspect(aspect,sentence,ad_words)
	m_score = 0
	m_probability = 0
	m_aspect = "general"
	for aspect in feature_list:
		if power[aspect][0] > m_probability:
			m_aspect = aspect
			m_probability = power[aspect][0]
			m_score = power[aspect][1]
	print(m_aspect)

	if(m_aspect in score_map.keys()):
		score_map[m_aspect] += m_score
		feature_word_map[m_aspect] += rel_words
	else:
		score_map[m_aspect] = m_score
		feature_word_map[m_aspect] = rel_words
	result_header_map[count] = m_aspect

def my_read_file():
	count = 1
	file_in = open("testfile.txt","r")
	for line in file_in:
		understand_sentence(line,count)
		count += 1

my_read_file()

def print_output():
	file_out_text.write("result_header_map = " + str(result_header_map))

print_output()