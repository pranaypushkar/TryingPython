filename = input("Enter the filename or Path: ")
fileObj = open(filename)
content = fileObj.read()
print(content)