from testfile_header import *
from testresult_header import *
from database import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

#anotated_data = open("testfile_header.py",'r')
#final_result = open("testresult_header.py",'r')
file_out_text = open("prec_recall_result.py",'w')
aspect_given = [];
aspect_found = [];
aspect_correct = [];


def find_aspect(unstemmed_noun):
	lmtzr = WordNetLemmatizer()
	word = lmtzr.lemmatize(unstemmed_noun)
	aspect_list = []
	if word in feature_list:
		aspect_list.append(word)
	count = 0
	for syns in processed_data:
		if word in syns:
			aspect_list.append(feature_list[count])
		else:
			count += 1
	return aspect_list

new_header_map = {}
count = 0

for lists in header_map.keys():
	count += 1
	aspect_list = []
	for words in header_map[lists]:
		words = words.strip()
		words = words.split(' ')
		for word in words:
			aspect_list += find_aspect(word)
	aspect_list = list(set(aspect_list))
	new_header_map[count] = aspect_list
		  
# print new_header_map
for i in range(len(feature_list)):
	aspect_given.append(0)
	aspect_found.append(0)
	aspect_correct.append(0)

for j in range(len(feature_list)):
	count = 1
	for count in range(1,len(header_map) + 1):
		if feature_list[j] in new_header_map[count]:
			aspect_given[j] += 1
		if feature_list[j] in result_header_map[count]:
			aspect_found[j] += 1
		if feature_list[j] in new_header_map[count] and feature_list[j] in result_header_map[count]:
			for k in range(len(feature_list)):
				if feature_list[k] in new_header_map[count] and k != j:
					aspect_given[k] -= 1
				
			aspect_correct[j] += 1
#print aspect_given
#print aspect_found
#print aspect_correct
precision = [];
recall = [];
for i in range(len(feature_list)):
	if aspect_found[i] != 0:
		precision.append(100.0 * aspect_correct[i]/ aspect_found[i])
	else:
		precision.append(-1)
	if aspect_given[i] != 0:
		recall.append(100.0 * aspect_correct[i]/ aspect_given[i])
	else:
		recall.append(-1)

file_precision_recall = open("plotter/precision_data.py","w")
file_precision_recall.write("feature_list = " + str(feature_list) + "\n")
file_precision_recall.write("precision = " + str(precision) + "\n")
file_precision_recall.write("recall = " + str(recall) + "\n")

		
