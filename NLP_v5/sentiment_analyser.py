from database import *
from senti_train_data import *
from testfile_header import *
from testresult_header import *
from extract_bag_count import *
from bag_of_words import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

from nltk.classify import SklearnClassifier
from sklearn.svm import SVC

# from nltk.classify import maxent

correct_aspect_map = {}
correct_score_map = {}
result_score_map = {}
feature_word_map = {}
pos_score_map = {}
neg_score_map = {}


def trained_classifier():
  # return maxent.MaxentClassifier.train(train_data)
  # return SklearnClassifier(SVC(), sparse=False).train(senti_train_data)
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
      features.append(get_senti_word_for_number(word))  
  
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
  print("SENTIMENT ANALYSIS STARTING...")
  file_in = open("testfile.txt","r")
  for line in file_in:
    if(count%3 == 0):
      print(str(100*count/30) +"%  Done..")
    understand_sentence(line,count,classifier)
    count += 1

my_read_file()

def print_output(percentage,percentage_senti):
  file_out = open("plotter/plot_data.py","w")
  file_result = open("plotter/result_data.py","w")
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
  file_out.write("percentage = " + str(percentage) + "\n")
  file_out.write("percentage_senti = " + str(percentage_senti))
  
  file_result.write("sentence_map = " + str(sentence_header_map) + "\n")
  file_result.write("score_map = " + str(result_score_map) + "\n")
  file_result.write("correct_score_map = " + str(correct_score_map) + "\n")
  file_result.write("correct_aspect_map = " + str(correct_aspect_map) + "\n")
  file_result.write("aspect_map = " + str(result_header_map))
 
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

count = 0
aspect_correct_count = 0
senti_correct_count = 0

for lists in header_map.keys():
  count += 1
  for words in header_map[lists]:
    words = words.strip()
    words = words.split(' ')
    found = False
    for word in words:
      correct_list = find_aspect(word)
      if(len(correct_list) > 0):
        correct_aspect_map[count] = correct_list[0]
      if(result_header_map[count] in find_aspect(word)):
        correct_aspect_map[count] = result_header_map[count]
        aspect_correct_count += 1
        found = True
      break
    if(found):
      break
  correct_score_map[count] = score_map[lists][0]
  if(result_score_map[lists] in score_map[lists]):
    correct_score_map[count] = result_score_map[lists]
    senti_correct_count += 1


print_output(aspect_correct_count*100.0/(count*1.0),senti_correct_count*100.0/(count*1.0))