import os, sys
print(sys.argv[0])
print(sys.argv[1])

f = open(sys.argv[0])
lines = f.readlines()
i = 1
for line in lines:
	print("{} {}".format(i,line))
	i += 1