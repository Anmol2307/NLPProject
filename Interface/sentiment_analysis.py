from testresult_header import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

# from nltk.classify import SklearnClassifier
# from sklearn.svm import SVC
# from nltk.classify import maxent

import sys
sys.path.insert(0, '../NLP_v4')
from senti_train_data import *
from database import *
from extract_bag_count import *

result_score_map = {}
feature_word_map = {}
pos_score_map = {}
neg_score_map = {}


def trained_classifier():
	# return maxent.MaxentClassifier.train(train_data)
	# return SklearnClassifier(SVC(), sparse=False).train(train_data)
	return nltk.classify.NaiveBayesClassifier.train(senti_train_data)


def numeric_for_aspect(aspect):
	count = 0
	for asp in feature_list:
		if(aspect == asp):
			return count
		count += 1
	return -1


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

def get_relevant_words(sentence):
	return get_non_nouns(sentence)

def understand_sentence(sentence,count,classifier):
	useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
	for characters in useless:
		sentence = sentence.replace(characters,"")
	sentence = sentence.strip()
	sentence = sentence.lower()
	dictionary = create_senti_dictionary(sentence)
	m_aspect = result_header_map[count]

	features = []
	features = get_relevant_words(sentence)
	# for word in dictionary.keys():
	# 	if(dictionary[word]) > 0:
	# 		features.append(word)
	
	dictionary["ASPECT"] = numeric_for_aspect(m_aspect)
	m_score = classifier.classify_many([(dictionary)])[0]

	if(m_aspect in pos_score_map.keys()):
		if(m_score >= 0):
			neg_score_map[m_aspect] -= 0
			pos_score_map[m_aspect] += m_score
		else:
			pos_score_map[m_aspect] += 0
			neg_score_map[m_aspect] -= m_score

		feature_word_map[m_aspect] += features
	else:
		if(m_score >= 0):
			neg_score_map[m_aspect] = 0
			pos_score_map[m_aspect] = m_score
		else:
			pos_score_map[m_aspect] = 0 
			neg_score_map[m_aspect] = -1.0*m_score
			
		feature_word_map[m_aspect] = features
	result_score_map[count] = m_score


def my_read_file():
	classifier = trained_classifier()
	count = 1
	file_in = open("testfile.txt","r")
	for line in file_in:
		understand_sentence(line,count,classifier)
		count += 1
my_read_file()

def print_output():
	file_out = open("../plotter/plot_data.py","w")
	feature_list = []
	pos_score_list = []
	neg_score_list = []
	for pair in pos_score_map.keys():
		feature_list.append(pair)
		pos_score_list.append(pos_score_map[pair])
		neg_score_list.append(neg_score_map[pair])

	file_out.write("poslabels = " + str(feature_list) + "\n")
	file_out.write("posvalues = " + str(pos_score_list) + "\n")
	file_out.write("negvalues = " + str(neg_score_list) + "\n")

	file_out.write("feature_graph = " + str(feature_word_map) + "\n")
	file_out.write("percentage = " + str(-1) + "\n")
	file_out.write("percentage_senti = " + str(-1))

print_output()