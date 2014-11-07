#!/usr/bin/python

inputFile = open('new_data_file.txt', "r")
parsed_array = []

prev_header = []

for line in inputFile :
	line.strip()
	if "##" in line:
		split_line = line.split("##")
		if split_line[0] != '':
			prev_header = []
			if "[" in split_line[0]:
				aspect_list = split_line[0].split(",")
				for aspect in aspect_list:
					if "[" in aspect:
						header = aspect.split("[")
						header[1] = header[1].replace("]","")
						prev_header.append([header[0],header[1]])
						parsed_array.append([header[0],header[1],split_line[1]])
		# elif prev_header != []:
		#  	for pairs in prev_header:
		#  		parsed_array.append([pairs[0],pairs[1],split_line[1]])
