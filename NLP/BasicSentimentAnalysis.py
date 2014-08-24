import nltk
import similarity
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import re
from pos_list import pos_list
from neg_list import neg_list
from nltk.tokenize.punkt import PunktWordTokenizer

s = raw_input("Enter An Input Text\n")
feature_list=["price", "picture","battery","storage", "upgrade","hardware","feature","size","design","media","sound","service","help-care","overall"]

s1 = PunktWordTokenizer().tokenize(s)
print s1
s2 = nltk.pos_tag(s1)
print s2

NOUNS = ["NN","NNS","NNP", "NNPS"]
ADJECTIVE = ["JJ","JJR","JJS"]

def positive(word):
	for pos in pos_list:
		if word == pos:
			return True
	return False

def negative(word):
	for neg in neg_list:
		if word == neg:
			return True
	return False

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
    l_syns = list()
    lmtzr = WordNetLemmatizer()
    word = lmtzr.lemmatize(word)
    synsets = wn.synsets(word2)
    for synset in synsets:
        for i in range(0,len(synset.lemma_names)):
			if word == synset.lemma_names[i] and similarity.semantic_match(word,word2) == 1:
				l_syns.append( (word, word2))
				#print l_syns
				return l_syns
    return l_syns
    
#function for checking if 2 words are hypernyms or not
def check_hypernym(word, word2):
    """checks to see if word and word2 are hypernyms"""
    l_syns = list()
    synsets = wn.synsets(word2)
    
    for synset in synsets:
		for hypernym in synset.hypernyms():
			for ss in hypernym.lemmas: 
				if word == ss.name:
					 l_syns.append( (word, word2) )
					 #print l_syns
					 return l_syns	
    return l_syns


'''
	1.	CC	Coordinating conjunction
	2.	CD	Cardinal number
	3.	DT	Determiner
	4.	EX	Existential there
	5.	FW	Foreign word
	6.	IN	Preposition or subordinating conjunction
	7.	JJ	Adjective
	8.	JJR	Adjective, comparative
	9.	JJS	Adjective, superlative
	10.	LS	List item marker
	11.	MD	Modal
	12.	NN	Noun, singular or mass
	13.	NNS	Noun, plural
	14.	NNP	Proper noun, singular
	15.	NNPS	Proper noun, plural
	16.	PDT	Predeterminer
	17.	POS	Possessive ending
	18.	PRP	Personal pronoun
	19.	PRP$	Possessive pronoun
	20.	RB	Adverb
	21.	RBR	Adverb, comparative
	22.	RBS	Adverb, superlative
	23.	RP	Particle
	24.	SYM	Symbol
	25.	TO	to
	26.	UH	Interjection
	27.	VB	Verb, base form
	28.	VBD	Verb, past tense
	29.	VBG	Verb, gerund or present participle
	30.	VBN	Verb, past participle
	31.	VBP	Verb, non-3rd person singular present
	32.	VBZ	Verb, 3rd person singular present
	33.	WDT	Wh-determiner
	34.	WP	Wh-pronoun
	35.	WP$	Possessive wh-pronoun
	36.	WRB	Wh-adverb
'''



grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP,VP
  """

cp = nltk.RegexpParser(grammar)
s3 = cp.parse(s2)
print s3

nouns = []
adjective = []
for (a,b) in s2:
	if b in NOUNS:
		nouns.append(a)
	if b in ADJECTIVE:
		adjective.append(a)

print nouns
print adjective



list = re.findall("(NP[^)]*)",s3.pprint())
for words in list:
    print words
    if ("/JJ" in words and "/NN" in words):
        print "Yes"
        adjective = re.findall("[A-Za-z]*\/JJ",words)
        for i in adjective:
            adjective = i
            break
        adjective = adjective.replace("/JJ","")
        noun = re.findall("[A-Za-z]*\/NN",words)
        for i in noun:
            noun = i
            break
        noun = noun.replace("/NN","")
        print "Adjective : " + adjective
        if(positive(adjective)):
            print "Is a Positive Adjective For "
        else:
            if(negative(adjective)):
                print "Is a Negative Adjective For "
            else:
                print "Cant Say About The"

        print "Noun : " + noun


'''
TRIAL SENTENCES
1. This camera has a good focus
2. This camera has a poor resolution
3. This camera has nice picture quality


'''