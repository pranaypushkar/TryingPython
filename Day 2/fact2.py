#!/usr/bin/python

def fact (n):
	if n == 0 :
		return 1
	elif n < 0 :
		return "Factorial not defined"
	if n == 1:
		return n
	else :
		return n * fact(n-1)
		
def fact1 (n):
	if n == 0 :
		return 1
	elif n < 0 :
		return "Factorial not defined"
	if n == 1:
		return n
	else :
		return n * fact1(n-1)
	
if '__main__' == '__name__':
	print(fact(5))
	print(fact(6))
else:
	print(__name__)