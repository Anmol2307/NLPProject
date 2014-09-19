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

