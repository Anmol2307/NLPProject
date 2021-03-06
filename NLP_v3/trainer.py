from mlearn import *
from pos_list import pos_list
from neg_list import neg_list
from database import *
from similarity import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

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

probability_aspect_given_word = {}
count_word = {}
score_aspect_and_word = {}

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

def string_to_int(s):
  try:
    return float(s)
  except:
    return 0

def get_some_aspect_for(list_of_words):
	list_of_aspects = []
	for word in list_of_words:
		max_count =  0.0
		max_feature = ""
		for feature in feature_list:
			value = semantic_match(word,feature)
			if(max_count < value and value > 0.5):
				max_feature = feature
				max_count = value
		if(max_count > 0.0):
			list_of_aspects.append(max_feature)
	return list_of_aspects

for tuples in parsed_array:
  words = tuples[0].strip().lower().split()
  aspects = []
  for word in words:
    aspects += find_aspect(word)
#  if(aspects == []):
#  	aspects = get_some_aspect_for(words)
  if(aspects == []):
  	continue
  for aspect in aspects:
    value = string_to_int(tuples[1])

    tuples[2] = tuples[2].lower()
    
    useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n','/']
    sentence = tuples[2]
    for characters in useless:
      sentence = sentence.replace(characters,"")
    sentence = sentence.strip()
    
    sentence = remove_unnecessary(sentence)
    
    lmtzr = WordNetLemmatizer()
    for words in sentence:
      words = lmtzr.lemmatize(words)
    for words in sentence:
      phrase = aspect + "|" + words
      if (phrase in probability_aspect_given_word.keys()):
        probability_aspect_given_word[phrase] = probability_aspect_given_word[phrase] + 1
        score_aspect_and_word[phrase] = score_aspect_and_word[phrase] + value
      else:
        probability_aspect_given_word[phrase] = 1
        score_aspect_and_word[phrase] = value

      if words in count_word.keys():
        count_word[words] += 1
      else:
        count_word[words] = 1

for phrase in probability_aspect_given_word.keys():
  score_aspect_and_word[phrase] /= (1.0*probability_aspect_given_word[phrase])
  pair = phrase.split("|")
  probability_aspect_given_word[phrase] /= (1.0*count_word[pair[1]])

trained_model = open("trained_model.py","w")
trained_model.write("probability_aspect_given_word = " + str(probability_aspect_given_word) + "\n")
trained_model.write("score_aspect_and_word = " + str(score_aspect_and_word) + "\n")
