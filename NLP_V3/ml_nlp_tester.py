from database import *
from trained_model import *
from testfile_header import *
import math

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

file_out_text = open("testresult_header.py",'w')
result_header_map = {}
sentence_header_map = {}

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


def compute_for_aspect(aspect,sentence,ad_words):
  score = 0
  probability = 0
  count = 0
  for word in sentence:
    phrase = aspect + "|" + word
    if(phrase in probability_aspect_given_word.keys()):
      probability += probability_aspect_given_word[phrase]
      if(word in ad_words):
        score += score_aspect_and_word[phrase]
        count += 1
  # print(probability)
  if(count != 0):
    return [probability,(1.0*score)/(1.0*count)]
  else:
    return [probability,0]

feature_word_map = {}
score_map = {}

def understand_sentence(sentence,count):
  useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
  for characters in useless:
    sentence = sentence.replace(characters,"")
  sentence = sentence.strip()
  sentence = sentence.lower()
  print(count)
  print(sentence)
  rel_words = remove_unnecessary(sentence)
  ad_words = get_non_nouns(sentence)
  
  
  sentence = sentence.split()

  lmtzr = WordNetLemmatizer()
  for word in sentence:
    word = lmtzr.lemmatize(word)
  power = {}
  for aspect in feature_list:
    power[aspect] = compute_for_aspect(aspect,sentence,ad_words)
  m_score = 0
  m_probability = 0
  m_aspect = "general"
  for aspect in feature_list:
    if power[aspect][0] > m_probability:
      m_aspect = aspect
      m_probability = power[aspect][0]
      m_score = power[aspect][1]
  print(m_aspect + "\n")

  if(m_aspect in score_map.keys()):
    score_map[m_aspect] += m_score
    feature_word_map[m_aspect] += rel_words
  else:
    score_map[m_aspect] = m_score
    feature_word_map[m_aspect] = rel_words
  result_header_map[count] = m_aspect

def my_read_file():
  count = 1
  file_in = open("testfile.txt","r")
  for line in file_in:
    sentence_header_map[count] = line
    understand_sentence(line,count)
    count += 1

my_read_file()

def print_output(percentage):
  file_out = open("plotter/plot_data.py","w")
  feature_list = []
  score_list = []
  for pair in score_map.keys():
    feature_list.append(pair)
    score_list.append(score_map[pair])
  file_out.write("poslabels = " + str(feature_list) + "\n")
  file_out.write("posvalues = " + str(score_list) + "\n")

  file_out.write("feature_graph = " + str(feature_word_map) + "\n")
  file_out.write("percentage = " + str(percentage))
  file_out_text.write("sentence_header_map = " + str(sentence_header_map) + "\n")
  file_out_text.write("result_header_map = " + str(result_header_map))

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
correct_count = 0
for lists in header_map.keys():
  count += 1
  for words in header_map[lists]:
    words = words.strip()
    words = words.split(' ')
    found = False
    for word in words:
      if(result_header_map[count] in find_aspect(word)):
        correct_count += 1
        found = True
      break
    if(found):
      break

print_output(correct_count*100.0/(count*1.0))