from database import *
from train_data import *
from testfile_header import *
from extract_bag_count import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer


from nltk.classify import SklearnClassifier
from sklearn.svm import SVC

file_out_text = open("testresult_header.py",'w')

result_header_map = {}
feature_word_map = {}
score_map = {}
sentence_header_map = {}


def trained_classifier():
  # return maxent.MaxentClassifier.train(train_data)
  # return SklearnClassifier(SVC(), sparse=False).train(train_data)
  return nltk.classify.NaiveBayesClassifier.train(train_data)

def understand_sentence(sentence,count,classifier):
  useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
  for characters in useless:
    sentence = sentence.replace(characters,"")
  sentence = sentence.strip()
  sentence = sentence.lower()
  dictionary = create_dictionary(sentence)
  m_aspect = classifier.classify_many([(dictionary)])[0]
  m_score = 0

  if(m_aspect in score_map.keys()):
    score_map[m_aspect] += m_score
    feature_word_map[m_aspect] += []
  else:
    score_map[m_aspect] = m_score
    feature_word_map[m_aspect] = []
  result_header_map[count] = m_aspect


def my_read_file():
  classifier = trained_classifier()
  count = 1
  print("ASPECT ANALYSIS STARTING...")
  file_in = open("testfile.txt","r")
  for line in file_in:
    if(count%3 == 0):
      print(str(100*count/30) +"%  Done..")
    sentence_header_map[count] = line
    understand_sentence(line,count,classifier)
    count += 1

my_read_file()

def print_output():
  file_out_text.write("result_header_map = " + str(result_header_map) + "\n")
  file_out_text.write("sentence_header_map = " + str(sentence_header_map) + "\n")
print_output()