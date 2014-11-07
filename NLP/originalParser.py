
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

def original_parser(s2):
#PARSER
	grammar = r"""
	NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
	PP: {<IN><NP>}               # Chunk prepositions followed by NP
	VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
	CLAUSE: {<NP><VP>}           # Chunk NP,VP
	"""

	cp = nltk.RegexpParser(grammar)
	s3 = cp.parse(s2)
	print s3
	
	
list = re.findall("(NP[^)]*)",s3.pprint())
for words in list:
	print words
	if ("/JJ" in words and "/NN" in words):
		print "Yes found both"
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
		final_noun = noun
		if(noun in feature_list):
			final_noun = noun
		else:
			array_1 = processed_data[0]
			counter = 0
			for lists in array_1:
				if(noun in lists):
					break
				else:
					counter += 1
			if(counter >= len(feature_list)):
				final_noun = noun + "_NOT_FOUND"
			else:
				final_noun = feature_list[counter]
			
			array_2 = processed_data[0]
			counter = 0
			for lists in array_2:
				if(noun in lists):
					break
				else:
					counter += 1

			if(counter >= len(feature_list)):
				final_noun = noun + "_NOT_FOUND"
			else:
				final_noun = feature_list[counter]

		print "Sentiment : " + adjective
		if(positive(adjective)):
			print "Is a Positive Adjective For "
		else:
			if(negative(adjective)):
				print "Is a Negative Adjective For "
			else:
				print "Cant Say About The"

		print "Feature : " + final_noun
