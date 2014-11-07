from database import *
from testfile_header import *
from testresult_header import *


import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

from nltk.classify import maxent

feature_word_map = {}
pos_score_map = {}
neg_score_map = {}

def print_output(percentage,percentage_senti):
  file_out = open("plotter/plot_data.py","w")
  pos_score_list = []
  neg_score_list = []
  for feature in feature_list:
	pos_score_list.append(0)
	neg_score_list.append(0)
  for i in range(len(feature_list)):
	  count = 0
	  for lists in result_header_map.keys():
		  count += 1  
		  for j in range(len(result_header_map[count])):
			  if feature_list[i] == result_header_map[count][j]:
				  if result_score_map[count][j] == 1:
					  pos_score_list[i] += 1
				  else :
					  neg_score_list[i] += 1
  file_out.write("poslabels = " + str(feature_list) + "\n")
  file_out.write("posvalues = " + str(pos_score_list) + "\n")
  file_out.write("negvalues = " + str(neg_score_list) + "\n")
  feature_word_map = {}	
  file_out.write("feature_graph = " + str(feature_word_map) + "\n")
  file_out.write("percentage = " + str(percentage) + "\n")
  file_out.write("percentage_senti = " + str(percentage_senti))
		  


  # file_out_text.write("result_header_map = " + str(result_header_map))
  
#def arrange_output():

def list_sum(l):
	ans = 0
	for num in l:
		ans += num
	return ans*1.0/len(l) 	

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

count = 0
aspect_correct_count = 0
senti_correct_count = 0

for lists in header_map.keys():
  count += 1
  avg = list_sum(result_score_map)
  if avg >= 0 and 1 in score_map[count]:
	  senti_correct_count += 1
  if avg < 0 and -1 in score_map[count]:
	  senti_correct_count += 1
  for words in header_map[lists]:
    words = words.strip()
    words = words.split(' ')
    found = False
    for word in words:
		for feature in result_header_map[count]:
			if feature in find_aspect(word):
				aspect_correct_count += 1
				found = True
		break	
    if(found):
		break
	
  #if(result_score_map[lists] in score_map[lists]):
	


print_output(aspect_correct_count*100.0/(count*1.0),senti_correct_count*100.0/(count*1.0))
