from not_found_data import *
from database import *
from trained_model import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer


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

def understand_sentence(sentence):
  useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n']
  for characters in useless:
    sentence = sentence.replace(characters,"")
  sentence = sentence.strip()
  sentence = sentence.lower()

  rel_words = remove_unnecessary(sentence)
  ad_words = get_non_nouns(sentence)
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


  sentence = sentence.split()

  lmtzr = WordNetLemmatizer()
  for word in sentence:
    word = lmtzr.lemmatize(word)
  power = {}
  for aspect in feature_list:
    power[aspect] = compute_for_aspect(aspect,sentence,ad_words)
  m_probability = 0
  m_aspect = "general"
  for aspect in feature_list:
    if power[aspect][0] > m_probability:
      m_aspect = aspect
      m_probability = power[aspect][0]
  print(m_aspect + "\n")

  return m_aspect

no_list = []
yes_list = []

for tuples in not_found_data:
  words = tuples[0].strip().lower().split()
  
  tuples[2] = tuples[2].lower()
  sentence = tuples[2]
  aspect_guessed = understand_sentence(sentence)

  for aspect in words:
    if(aspect in no_list or aspect in yes_list):
      continue
    print("Guessing Aspect " + str(aspect) + " : " + str(aspect_guessed))
    yes_no = input("Want To Train?")
    if(yes_no == "STOP"):
    	break
    if(yes_no == "y"):
      yes_list.append(aspect)
      count = 0
      for words_list in feature_list:
        print(str(count) + " : " + words_list)  
        count+= 1
      count = input("What state?")
      processed_data[int(count)].append(aspect)
    else:
      no_list.append(aspect)

new_database = open("processed_database.py")
file_out.write("feature_list = " + str(feature_list))
file_out.write("processed_data = " + str(processed_data))
