# from sets import Set
from mlearn import *
from complete_senti_word import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

bag_of_words = set([])


def remove_unnecessary(sentence):
  s1 = PunktWordTokenizer().tokenize(sentence)
  s2 = nltk.pos_tag(s1)
  useful = ["JJ","JJS","JJS","NN","NNS","NNP","NNPS","RB","RBR","RBS"]
  splitted = []
  # print s2
  lmtzr = WordNetLemmatizer()
  for pairs in s2:
    if(pairs[1] in useful):
      splitted.append(lmtzr.lemmatize(pairs[0]))
  return splitted

count = 0
for tuples in parsed_array:
  if(count == 1):
    print("0% Complete..")
  if(count == 3500):
    print("50% Complete...")
  if(count == 7000):
    print("100% Complete....")
  words = tuples[0].strip().lower().split()
  useless = [',',':','.',';','"',"'",')','(','[',']','{','}','|','>','<','\t','\n','=']
  sentence = tuples[2]
  for characters in useless:
    sentence = sentence.replace(characters,"")
  sentence = sentence.strip()
  sentence = sentence.lower()
  sentence = remove_unnecessary(sentence)
  words += sentence
  for word in words:
    if(word in senti_bag_of_words):
      bag_of_words.add(word)



print("Accumulated The Senti Dictionary Of Size : " + str(len(bag_of_words)))
file_bag = open("senti_bag_of_words.py","w")
bag_of_words = list(bag_of_words)
file_bag.write("senti_bag_of_words = "+str(bag_of_words))
print("Printed The Senti Bag Of Words")   
