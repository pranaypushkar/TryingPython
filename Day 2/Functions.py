def total (a, b) :
	"""Display sum of two numbers
	or concatenated sring"""
	#print (a + b)
	print(total.__doc__)
	print (a + b)
	return (a + b)
	
print(total.__doc__)
result = total(10, 20); 
print(result)
help(total)
total("Good", "Morning")
