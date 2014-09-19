import re

def parseCommand(word,line):
	line = line.replace(word + "(","")
	line = line.replace(")","")
	line = line.split(",")
	line[0] = line[0].split("-")[0].strip()
	line[1] = line[1].split("-")[0].strip()
	return [word,line[0],line[1]]

def parseResult():
	list_of_commands = ["acomp","advmod","amod",
	"cc","conj","dobj","marker","neg","npadvmod",
	"nsubj","root","num","preconj","nn","conj_or","conj_and","conj_negcc"]
	
	net_commands_found = []
	commands_found = []


	data_file_address = "stanford_out.txt"
	file_in = open(data_file_address, 'r')
	
	for line in file_in:
		if(line == "(ROOT\n"):
			net_commands_found.append(commands_found)
			commands_found = []
			continue
		for word in list_of_commands:
			pattern = "(" + word + "\(.*\))"
			found = re.findall(pattern,line);
			if(len(found) > 0):
				commands_found.append(parseCommand(word,found[0]))
	net_commands_found.append(commands_found)
	return net_commands_found
