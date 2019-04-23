import sys
sys.setrecursionlimit(10000)

def fact (n):
	if n == 0 :
		return 1
	elif n < 0 :
		return "Factorial not defined"
	if n == 1:
		return n
	else :
		return n * fact(n-1)
		
result = fact(1500)
print(result)
