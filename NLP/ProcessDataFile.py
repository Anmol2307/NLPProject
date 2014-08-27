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
		if(pairs[1] in  NOUNS):
			result.append(pairs[0])
	return result

def processDataFile():
	file_noun_list = []

	data_file_address = "data_file_trimmed.txt"
	file_in = open(data_file_address, 'r')
	
	for line in file_in:
		s1 = PunktWordTokenizer().tokenize(line)
		s2 = nltk.pos_tag(s1)	
		noun_list = getNouns(s2)
		for noun in noun_list:
			lmtzr = WordNetLemmatizer()
			word = lmtzr.lemmatize(noun)
			file_noun_list.append(word)
	return file_noun_list

#function for checking if 2 words are synonyms or not
def check_synonym(word, word2):
	lmtzr = WordNetLemmatizer()
	word = lmtzr.lemmatize(word)
	synsets = wn.synsets(word2)
	for synset in synsets:
		for i in range(0,len(synset.lemma_names)):
			if(word == synset.lemma_names[i] and similarity.semantic_match(word,word2) == 1):
				return True
	return False
    
#function for checking if 2 words are hypernyms or not
def check_hypernym(word, word2):
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
			if((word == feature or check_synonym(word,feature)) and word not in feature_syn_list):
				feature_syn_list.append(word)
				continue
			if(check_hypernym(word,feature) and word not in feature_hyper_list):
				feature_hyper_list.append(word)
				continue
		syn_array.append(feature_syn_list)		
		hyper_array.append(feature_hyper_list)		

	return (syn_array,hyper_array)

def uniq(input):
	output = []
	for x in input:
		if x not in output:
			output.append(x)
	return output

file_noun_list = processDataFile()
syn_hyper_array = getSynAndHyperArrays(file_noun_list)


data_processed_file = "data_processed_file.py"
file_out = open(data_processed_file, 'w')
file_out.write("processed_data = " + str(syn_hyper_array))