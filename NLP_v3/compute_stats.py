from testfile_header import *
from testresult_header import *
from database import *

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

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
    if(result_header_map[count] in find_aspect(words)):
      correct_count += 1
      break

print correct_count*100.0/(count*1.0)