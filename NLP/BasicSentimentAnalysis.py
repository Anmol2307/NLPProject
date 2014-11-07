import nltk
import data_processed_file
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import re
from pos_list import pos_list
from neg_list import neg_list
from nltk.tokenize.punkt import PunktWordTokenizer
from data_processed_file import *

s = raw_input("Enter An Input Text\n")

s1 = PunktWordTokenizer().tokenize(s)
print s1
s2 = nltk.pos_tag(s1)
print s2

NOUNS = ["NN","NNS","NNP", "NNPS"]
ADJECTIVE = ["JJ","JJR","JJS"]

def positive(word):
	for pos in pos_list:
		if word == pos:
			return True
	return False

def negative(word):
	for neg in neg_list:
		if word == neg:
			return True
	return False

def request_update(word):
	wud_like_to = raw_input("Would You Like To Classify The Aspect? (Y/y)")
	if(wud_like_to == 'Y' or wud_like_to == 'y'):
		count = 0
		for words in feature_list:
			print words + "(" + str(count) + ")"
			count += 1
	update_into = raw_input("What do you classify this into?")
	update_data(word,int(update_into))

def update_data(word,position):


def print_updated_file():
	new_feature_list = feature_list
	new_processed_data = processed_data
	data_processed_file = "data_processed_file.py"
	file_out = open(data_processed_file, 'w')
	file_out.write("feature_list = " + str(new_feature_list))
	file_out.write("processed_data = " + str(new_processed_data))

nouns = []
adjective = []
for (a,b) in s2:
	if b in NOUNS:
		nouns.append(a)
	if b in ADJECTIVE:
		adjective.append(a)

print nouns
print adjective


# conjunctions = ["for","and","nor","but","or","yet",",","so"]

# nplist = re.findall("(NP[^)]*)",s3.pprint())
# for np_phrase in nplist:

grammar = r"""
NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>}               # Chunk prepositions followed by NP
VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
CLAUSE: {<NP><VP>}           # Chunk NP,VP
"""

cp = nltk.RegexpParser(grammar)
s3 = cp.parse(s2)
print s3
	
	
list = re.findall("(NP[^)]*)",s3.pprint())
for words in list:
	print words
	if ("/JJ" in words and "/NN" in words):
		print "Yes found both"
		adjective = re.findall("[A-Za-z]*\/JJ",words)
		for i in adjective:
			adjective = i
			break
		adjective = adjective.replace("/JJ","")
		noun = re.findall("[A-Za-z]*\/NN",words)
		for i in noun:
			noun = i
			break
		noun = noun.replace("/NN","")
		final_noun = noun
		noun_found = False
		if(noun in feature_list):
			final_noun = noun
			noun_found = True
		else:
			array_1 = processed_data[0]
			counter = 0
			for lists in array_1:
				if(noun in lists):
					noun_found = True
					break
				else:
					counter += 1
			if(counter >= len(feature_list)):
				final_noun = noun + "_NOT_FOUND"
			else:
				noun_found = True
				final_noun = feature_list[counter]
			
			array_2 = processed_data[0]
			counter = 0
			for lists in array_2:
				if(noun in lists):
					noun_found = True
					break
				else:
					counter += 1

			if(counter >= len(feature_list)):
				final_noun = noun + "_NOT_FOUND"
			else:
				noun_found = True
				final_noun = feature_list[counter]

		if(not noun_found):
			request_update(noun)
			
		print "Sentiment : " + adjective
		if(positive(adjective)):
			print "Is a Positive Adjective For "
		else:
			if(negative(adjective)):
				print "Is a Negative Adjective For "
			else:
				print "Cant Say About The"

		print "Feature : " + final_noun


'''
TRIAL SENTENCES
1. This camera has a good focus
2. This camera has a poor resolution
3. This camera has nice picture quality
'''	