import nltk
import similarity
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktWordTokenizer

feature_list=["price", "picture","battery","storage", "upgrade","hardware","feature","size","design","media","sound","service","help-care","overall"]

NOUNS = ["NN","NNS","NNP", "NNPS"]
ADJECTIVE = ["JJ","JJR","JJS"]

def getNouns(tag_list):
	result = []
	for pairs in tag_list:
		if(pairs[1] in  NOUNS)
			result.append(pairs[0])

def processDataFile():
	file_noun_list = []

	data_file_address = "data_file.txt"
	data_processed_file = "data_processed_file.txt"
	file_in = open(dataFileAddress, 'r')
	file_out = open(data_processed_file, 'w')
	
	for line in f:
		s1 = PunktWordTokenizer().tokenize(line)
		s2 = nltk.pos_tag(s1)	
		noun_list = getNouns(s2)
		for nouns in noun_list:
			lmtzr = WordNetLemmatizer()
			word = lmtzr.lemmatize(noun)
			file_noun_list.append(word)
	return file_noun_list

#function for checking if 2 words are synonyms or not
def check_synonym(word, word2):
    """checks to see if word and word2 are synonyms"""
    #l_syns = list()
    lmtzr = WordNetLemmatizer()
    word = lmtzr.lemmatize(word)
    synsets = wn.synsets(word2)
    for synset in synsets:
        for i in range(0,len(synset.lemma_names)):
			if word == synset.lemma_names[i] and similarity.semantic_match(word,word2) == 1:
				#l_syns.append( (word, word2))
				#print l_syns
				return True
    return False
    
#function for checking if 2 words are hypernyms or not
def check_hypernym(word, word2):
    """checks to see if word and word2 are hypernyms"""
    #l_syns = list()
    synsets = wn.synsets(word2)
    
    for synset in synsets:
		for hypernym in synset.hypernyms():
			for ss in hypernym.lemmas: 
				if word == ss.name:
					 #l_syns.append( (word, word2) )
					 #print l_syns
					 return True	
    return False

def getSynAndHyperArrays(file_noun_list):
	syn_array = []
	hyper_array = []
	for feature in feature_list:
		feature_syn_list = []
		feature_hyper_list = []
		for word in file_noun_list:
			if(word == feature or check_synonym(word,feature)):
				feature_syn_list.append(word)
				continue
			if(check_hypernym(word,feature)):
				feature_hyper_list.append(word)
				continue
		syn_array.append(feature_syn_list)		
		hyper_array.append(feature_hyper_list)		

	return (syn_array,hyper_array)

file_noun_list = processDataFile()
syn_hyper_array = getSynAndHyperArrays(file_noun_list)