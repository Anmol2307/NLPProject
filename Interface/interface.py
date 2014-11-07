file_output = open("testfile.txt","w")
print("INPUT YOUR COMMENTS BELOW, FOLLOWED BY A 'DONE'")
while(True):
	input_text = input("")
	if(input_text == "DONE"):
		break
	sentences = input_text.split('.')
	for sentence in sentences:
		sentence.strip()
		if(sentence == ""):
			continue
		file_output.write(sentence + " .\n")