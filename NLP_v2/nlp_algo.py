import nltk
from similarity import *
from pos_list import pos_list
from neg_list import neg_list
from database import *

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from parse_stanford import *

what_we_know = [];
file_out_text = open("testresult_header.py",'w')
result_header_map = {}
score_map = {}

#~ print(feature_list)
max_corr=0
def close_match(feature):
	global max_corr
	max_corr = 0
	ans = feature_list[0]
	for word in feature_list:
		corr = semantic_match(word, feature)
		if corr >= max_corr:
			max_corr = corr
			ans = word
	return ans
			

def find_aspect(unstemmed_noun):
	lmtzr = WordNetLemmatizer()
	word = lmtzr.lemmatize(unstemmed_noun)
	if word in feature_list:
		return word
	count = 0
	for syns in processed_data:
		if word in syns:
			return feature_list[count]
		else:
			count += 1
	return close_match(word)

def find_sentiment_type(word):
	for pos in pos_list:
		if word == pos:
			return "positively"
	for neg in neg_list:
		if word == neg:
			return "negatively"
	return "unknown"

'''
This following function is to deal with 
adjectives and adverbs relations to aspects 
in the dependency parsed result
i.e. 
advmod / amod (ASPECT,SENTIMENT)

THis also checks if an aspect is the subject of a another noun:
	this is case of direct comments like:
	"focus is awesome"
'''
def matchAorAdvMod(commands):
	global what_we_know
	for command in commands:
		if(command[0] == "amod" or command[0] == "advmod"):
			aspect = find_aspect(command[1])
			sentiment_type = find_sentiment_type(command[2])
			if(aspect == "unknown feature" and sentiment_type == "unknown"):
				continue			
			what_we_know.append(["ADJ",command[1],command[2],0]);
			#print command[2] + " is " + sentiment_type + " for aspect " + aspect
		if(command[0] == "nsubj"):
			aspect = find_aspect(command[2])
			sentiment_type = find_sentiment_type(command[1])
			if(aspect == "unknown feature" and sentiment_type == "unknown"):
				continue			
			what_we_know.append(["ADJ",command[2],command[1],0]);


'''
This deals with conjuctions relating 
two features of the commodity.
i.e.
conj / conj_and / conj_or (ASPECT_1, ASPECT_2)
It checks if the aspects already have adjectives attached to them.
If they dont the adjective of the other gets propogated to it.
'''
def matchConjunctions(commands):
	global what_we_know
	conjunctions = ["conj_and","conj","conj_or"]
	for command in commands:
		if(not (command[0] in conjunctions)):
			continue
		found_w1 = False
		found_w2 = False
		adj_w1 = ''
		adj_w2 = ''
		for words in what_we_know:
			if(words[1] == command[1]):
				found_w1 = True
				adj_w1 = words[2]
			if(words[1] == command[2]):
				found_w2 = True
				adj_w2 = words[2]
		if(not(found_w1) and not(found_w2)):
			continue
		if(found_w2 and found_w1):
			continue
		if(found_w1 and not(found_w2)):
			what_we_know.append(["ADJ",command[2],adj_w1,0])
		if(found_w2 and not(found_w1)):
			what_we_know.append(["ADJ",command[1],adj_w2,0])

def matchPureNeg(commands):
	for command in commands:
		if(not (command[0] == "neg")):
			continue
		aspect_word = "";
		for dobjcommand in commands:
			if(not(dobjcommand[0] == "dobj" and dobjcommand[1] == command[1])):
				continue
			aspect_word = dobjcommand[2]
			break
		if(aspect_word == ""):
			aspect_word = command[1]

		changed = []
		for words in what_we_know:
			if(words[1] == aspect_word):
				words[3] = 1 - words[3]
				changed = [words[0],"",words[2],words[3]]

		if(changed == []):
			continue

		#print aspect_word + " : " + command[1] + " : " 
		#print what_we_know
		for conj_or_obj in commands:
			if(not(
				(conj_or_obj[0] == "conj_or" \
					or (conj_or_obj[0] == "conj_and" 
						and not(aspect_word == command[1]))) \
					and conj_or_obj[1] == command[1])):
				continue
			changed[1] = conj_or_obj[2]
			what_we_know.append(changed)
		
		for conj_and_obj in commands:
			if(not(conj_and_obj[0] == "conj_and" 
				and conj_and_obj[1] == aspect_word)):
				continue
			if(conj_and_obj[1] == aspect_word):
				for words in what_we_know:
					if(words[1] == conj_and_obj[2]):
						words[3] = 1 - words[3]

def matchConjNeg(commands):
	for command in commands:
		if(not (command[0] == "conj_negcc")):
			continue
		found_w1 = False
		found_w2 = False
		adj_w1 = ''
		adj_w2 = ''
		count = 0
		w1_count = 0
		w2_count = 0
		
		for words in what_we_know:
			if(words[1] == command[1]):
				found_w1 = True
				adj_w1 = words[2]
				w1_count = count
			if(words[1] == command[2]):
				found_w2 = True
				adj_w2 = words[2]
				w2_count = count
			count += 1

		if(not(found_w1) and not(found_w2)):
			for words in what_we_know:
				if(words[2] == command[2]):
					words[3] = 1 - words[3]
		if(found_w2 and found_w1):
			what_we_know[w2_count][3] = 1 - what_we_know[w2_count][3]
		if(found_w1 and not(found_w2)):
			what_we_know.append(["ADJ",command[2],adj_w1, 1 - what_we_know[w1_count][3]])
		if(found_w2 and not(found_w1)):
			continue

aspect_list = []
sentiment_list = []
def printWhatWeKnow():
	count = 1
	global aspect_list,sentiment_list
	aspect_list = []
	sentiment_list = []
	
	for words in what_we_know:
		negation = 1
		aspect = find_aspect(words[1])
		if aspect != "unknown feature":
			aspect_list.append(str(aspect))
		else:
			aspect_list.append("general")
		sentiment_type = find_sentiment_type(words[2])
		if sentiment_type == "negatively":
			negation = -1	
			
		append_word = ""
		if(words[3] == 1):
			append_word = "NOT "
			negation *= -1
			
		sentiment_list.append(negation)
		
		print str(count) + ".\t"
		print "\t" + str(words)
		print "\t" + words[2] + " is " + append_word + "saying " + sentiment_type + " for the aspect " + aspect + "\n"
		count += 1

#print "Loading the Stanford Results..."
#print "Processing and Implementing Sentiment Analysis...\n\n"

line_number = 1
for commands in  parseResult():
	if(commands == []):
		continue
	print "LINE " + str(line_number) + " : "
	what_we_know = []
	matchAorAdvMod(commands)
	matchConjunctions(commands)
	matchPureNeg(commands)
	matchConjNeg(commands)
	printWhatWeKnow()
	#aspect_list = list(set(aspect_list))
	result_header_map[line_number] = aspect_list
	score_map[line_number] = sentiment_list
	line_number += 1

file_out_text.write("result_header_map = " + str(result_header_map) + "\n")
file_out_text.write("score_map = " + str(score_map))
