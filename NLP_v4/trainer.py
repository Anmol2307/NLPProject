from mlearn import *
from extract_bag_count import *
from database import *

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
#  if(aspect_list == []):
#    return [close_match(word)]
  return aspect_list

probability_aspect_given_word = {}
count_word = {}
score_aspect_and_word = {}

'''
from similarity import *

def close_match(feature):
  max_corr = 0
  result = "general"
  for word in feature_list:
    corr = semantic_match(word, feature)
    if corr > max_corr:
      max_corr = corr
      result = word
  return result
'''

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
    a = float(s)
    if(a > 0):
      return 1
    else:
      return -1
  except:
    return 0

def numeric_for_aspect(aspect):
  count = 0
  for asp in feature_list:
    if(aspect == asp):
      return count
    count += 1
  return -1

train_data = []
senti_train_data = []

for tuples in parsed_array:
  value = string_to_int(tuples[1])
  tuples[2] = tuples[2].lower()
  useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
  sentence = tuples[2]
  value = string_to_int(tuples[1])
  for characters in useless:
    sentence = sentence.replace(characters,"")
  sentence = sentence.strip()
  sentence = sentence.lower()
  dictionary = create_dictionary(sentence)
  senti_dictionary = create_senti_dictionary(sentence)
  senti_dictionary["ASPECT"] = ""

  words = tuples[0].strip().lower().split()
  aspects = []
  for word in words:
    aspects += find_aspect(word)
  if(aspects == []):
    continue
  for aspect in aspects:
    senti_dictionary["ASPECT"] = numeric_for_aspect(aspect)
    train_data.append((dictionary,aspect))
    senti_train_data.append((senti_dictionary,value))


file_data = open("train_data.py","w")
file_data.write("train_data = "+str(train_data) + "\n")
file_data = open("senti_train_data.py","w")
file_data.write("senti_train_data = "+str(senti_train_data))
    
