from result_data import *

detailed_file = open("js/detailed.js", 'w')

def process(print_file,tpl_list):
	strng = '<table>'
	strng += '<tr><th>No</th>'
	strng += '<th>Sentence</th>'
	strng += '<th>Guessed Aspect</th>'
	strng += '<th>True Aspect</th>'
	strng += '<th>Guessed Sentiment</th>'
	strng += '<th>True Sentiment</th></tr>'
	for tpl in tpl_list:
		str_extra = 'class = \'correct_aspect\''
		if(tpl[5] != tpl[4]):
			str_extra = 'class = \'incorrect_aspect\''
		elif(tpl[2] != tpl[3]):
			str_extra = 'class = \'incorrect_score\''

		strng += '<tr ' + str_extra + '>'
		strng += '<td><b>' + str(tpl[0]) + '</b></td>'
		strng += '<td>' + str(tpl[1].strip()) + '</td>'
		strng += '<td>' + str(tpl[5]) + '</td>'
		strng += '<td>' + str(tpl[4]) + '</td>'
		strng += '<td>' + str(tpl[2]) + '</td>'
		strng += '<td>' + str(tpl[3]) + '</td>'
		strng += '</tr>'
	strng += '</table>'

	print_file.write('$(function(){\n')
	print_file.write('$("#stat_details").html("'+ strng+'")')
	print_file.write('});')

total_data = []
for count in sentence_map.keys():
	# print(count)
	data_tuple = (
		count,
		sentence_map[count],
		score_map[count],
		correct_score_map[count],
		correct_aspect_map[count],
		aspect_map[count]
		)
	total_data.append(data_tuple)

process(detailed_file,total_data)