def avg(l):
	"""
	>>> print(avg([10, 20, 30, 40]))
	25
	"""
	return sum(l)/len(l)
	
	
import doctest
doctest.testmod()