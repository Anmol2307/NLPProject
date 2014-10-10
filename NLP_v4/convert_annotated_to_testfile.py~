inputFile = open('annotated_testbench', "r")
parsed_array = []
file_out = open('testfile.txt','w')
file_out_header = open('testfile_header.py','w')

header_map = {}
count = 1
for line in inputFile :
  line.strip()
  if "##" in line:
    split_line = line.split("##")
    if split_line[0] != '':
      file_out.write(split_line[1].strip() + "\n")
      if "[" in split_line[0]:
        aspect_list = split_line[0].split(",")
        for aspect in aspect_list:
          if "[" in aspect:
            header = aspect.split("[")
            header[1] = header[1].replace("]","")
            parsed_array.append([header[0],header[1],split_line[1]])
            if(header_map.has_key(count)):
              header_map[count].append(header[0])
            else:
              header_map[count] = [header[0]]
  count += 1

file_out_header.write("header_map = " + str(header_map))

