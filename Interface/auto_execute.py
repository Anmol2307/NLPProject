file_output = open("testfile.txt","w")
input_text_file = open("input.txt","r")

input_text = input_text_file.read().replace('\n','.')
sentences = input_text.split('.')
for sentence in sentences:
	sentence.strip()
	if(sentence == "" or len(sentence.split(' ')) <= 3):
		continue
	file_output.write(sentence + " .\n")
