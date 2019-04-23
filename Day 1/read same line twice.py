import os, sys

source = open("C:\\Users\\Admin\\Desktop\\My Scripts\\Test.txt")
loc = source.tell()
content = source.readline()
while content != "" :
	print(content)
	source.seek(loc)
	content = source.readline()
	print(content)
	loc = source.tell()
	content = source.readline()
source.close()
raw_input()