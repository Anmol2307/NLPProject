from mlearn import *
from extract_bag_count import *
from database import *
from svmutil import *

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
    a = float(s)
    if(a > 0):
      return 1
    else:
      return -1
  except:
    return 0

def numeric_for_aspect(aspect):
  count = 00
  for asp in feature_list:
    if(aspect == asp):
      return count
    count += 1
  return -1
  
def dict_to_str(dic, label):
  s = str(label)
  s += " "
  i = 1
  for key,value in dic.items():
    s += str(i) 
    s += ":"
    s += value 
    s += ' '
    i += 1
  return s
  
train_data_dictionary = []
train_data_value = []
senti_train_data_dictionary = []
senti_train_data_value = []

# file_senti_train = open("svm_senti_train.py","w")
# file_train = open("svm_train.py","w")

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
    senti_dictionary[0] = numeric_for_aspect(aspect)
    train_data_dictionary.append(dictionary)
    train_data_value.append(numeric_for_aspect(aspect))
    senti_train_data_dictionary.append(senti_dictionary)
    senti_train_data_value.append(value)

m = svm_train(train_data_value,train_data_dictionary)
svm_save_model('svm_data.model', m)