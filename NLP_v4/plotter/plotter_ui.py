from plot_data import *
from precision_data import *

stats_file = open("js/statistics.js", 'w')
relation_file = open("js/relations.js", 'w')

def printChart(print_file,labels,values1,values2,id,rgb1,rgb2):
	print_file.write('$(function(){\n')
	print_file.write('var ctx = document.getElementById("' + id + '").getContext("2d");\n')
	print_file.write('var data = {labels:\n')
	print_file.write(str(labels))
	print_file.write(',\n')
	print_file.write('datasets: [\n')
	print_file.write('{\n')
	print_file.write('label: "Sentiment Analysed",\n')
	print_file.write('fillColor: "rgba('+ rgb1 +',0.5)",\n')
	print_file.write('strokeColor: "rgba('+ rgb1 +',0.8)",\n')
	print_file.write('highlightFill: "rgba('+ rgb1 +',0.75)",\n')
	print_file.write('highlightStroke: "rgba('+ rgb1 +',1)",\n')
	print_file.write('data:\n')
	print_file.write(str(values1))
	print_file.write('}\n')
	print_file.write(',\n')
	print_file.write('{\n')
	print_file.write('label: "Sentiment Analysed",\n')
	print_file.write('fillColor: "rgba('+ rgb2 +',0.5)",\n')
	print_file.write('strokeColor: "rgba('+ rgb2 +',0.8)",\n')
	print_file.write('highlightFill: "rgba('+ rgb2 +',0.75)",\n')
	print_file.write('highlightStroke: "rgba('+ rgb2 +',1)",\n')
	print_file.write('data:\n')
	print_file.write(str(values2))
	print_file.write('}\n')
	print_file.write(']};\n')
	print_file.write('var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});\n')
	print_file.write('});\n')

def printDoughChart(print_file,percentage,id):
	print_file.write('$(function(){\n')
	print_file.write('var ctx = document.getElementById("'+ id +'").getContext("2d");\n')
	print_file.write('var value_div = document.getElementById("'+ id +'Value");\n')
	print_file.write('value_div.innerHTML = "'+ str(percentage)+'%";\n')
	print_file.write('var data = [\n')

	print_file.write('{\n')
	print_file.write('value: ' + str(100.0 - percentage) + ',\n')
	print_file.write('color:"#F7464A",\n')
	print_file.write('highlight: "#FF5A5E",\n')
	print_file.write('label: "Not Done"\n')
	print_file.write('}\n')

	print_file.write(',\n')

	print_file.write('{\n')
	print_file.write('value: ' + str(percentage) + ',\n')
	print_file.write('color: "#2baf2b",\n')
	print_file.write('highlight: "#42bd41",\n')
	print_file.write('label: "Done"\n')
	print_file.write('}\n')

	print_file.write('];\n')
	print_file.write('var myDoughnutChart = new Chart(ctx).Doughnut(data,{animationSteps: 200,animationEasing : "easeOutQuart"});\n')
	print_file.write('});\n')

printChart(stats_file,poslabels,posvalues,negvalues,"posChart","37,155,36","232,78,64")
# printChart(stats_file,poslabels,negvalues,"negChart","232,78,64")
printDoughChart(stats_file,percentage,"perChart")
printDoughChart(stats_file,percentage_senti,"sentiPerChart")

def print_graph(print_file,id,label,aspects):
	# print_file.write('<div id="container_'+id+'"></div>\n')
	# print_file.write('<script type="text/javascript">\n')
	print_file.write('$(function(){\n')
	print_file.write('var nodes_'+id+' = [\n')
	print_file.write('{id: 1, label: "' + label + '"},\n')
	count = 2
	for words in aspects:
		print_file.write('{id: ' + str(count) + ', label: "'+ str(words)+'"},\n')
		count += 1
	print_file.write('];\n')
	print_file.write('var edges_'+id+' = [\n')
	count = 2
	for words in aspects:
		print_file.write('{from: 1, to: ' + str(count) + '},\n')
		count += 1
	print_file.write('];\n')
	print_file.write('var container_'+id+' = document.getElementById("container_'+id+'");\n')
	print_file.write('var data_'+id+'= {\n')
	print_file.write('nodes: nodes_'+id+',\n')
	print_file.write('edges: edges_'+id+'\n')
	print_file.write('};\n')
	print_file.write('var options_'+id+' = {\n')
	print_file.write('width: "600px",\n')
	print_file.write('height: "600px"\n')
	print_file.write('};\n')
	print_file.write('var network_'+id+' = new vis.Network(container_'+id+', data_'+id+', options_'+id+');\n')
	print_file.write('});\n')
	# print_file.write('</script>\n')

count = 1
def removeDuplicates(array):
	processArray = []
	for words in array:
		if words not in processArray:
			processArray.append(words)
	return processArray

for word_map in feature_graph.keys():
	# if(len(feature_graph[word_map]) < 15):
	print_graph(relation_file ,str(count),word_map,removeDuplicates(feature_graph[word_map]))
	count += 1


def printTableData(print_file,label,precision,recall):
	print_file.write('$(function(){\n')
	print_file.write('var table = document.getElementById("precision_table");\n')
	output_str = ''
	count = 0
	final_label = []
	final_precision = []
	final_recall = []
	for word in label:
		if(precision[count] != -1):
			output_str += '<tr><td>'
			output_str += str(label[count])
			output_str += '</td><td>'
			output_str += str(precision[count])
			output_str += '</td><td>'
			output_str += str(recall[count])
			output_str += '</td></tr>'
			final_label.append(label[count])
			final_precision.append(precision[count])
			final_recall.append(recall[count])
		count += 1

	print_file.write('table.innerHTML = "' + output_str + '"\n')
	print_file.write('});\n')
	return [final_label,final_precision,final_recall]

result = printTableData(stats_file,feature_list,precision,recall)
printChart(stats_file,result[0],result[1],result[2],"negChart","86,119,252","255,152,0")
