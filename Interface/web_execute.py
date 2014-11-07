import re
file_name = open("input.xml","r")
html = file_name.read()
notag = re.sub("<.*?>", " ", html)
file_out = open("input.txt","w")
file_out.write(notag)