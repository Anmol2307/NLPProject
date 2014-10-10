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
score_map = {}


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

def understand_sentence(sentence,count,classifier):
  useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
  for characters in useless:
    sentence = sentence.replace(characters,"")
  sentence = sentence.strip()
  sentence = sentence.lower()
  dictionary = create_senti_dictionary(sentence)
  m_aspect = result_header_map[count]

  features = []
  for word in dictionary.keys():
    if(dictionary[word]) > 0:
      features.append(word)
  
  dictionary["ASPECT"] = numeric_for_aspect(m_aspect)
  m_score = classifier.classify_many([(dictionary)])[0]

  if(m_aspect in score_map.keys()):
    score_map[m_aspect] += m_score
    feature_word_map[m_aspect] += features
  else:
    score_map[m_aspect] = m_score
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
  print(result_header_map[1] + " " + str(result_score_map[1]))
  # file_out_text.write("result_header_map = " + str(result_header_map))

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

print_output()