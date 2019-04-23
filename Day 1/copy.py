import os, sys

source = open(sys.argv[1])
dest = open(sys.argv[2], 'w')
content = source.readlines()
dest.writelines(content)
source.close()
dest.close()