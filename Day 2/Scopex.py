#! /usr/bin/python								#scopex.python
a, b, c, d,  = 10, 20, 30, 40
def FunA():
	a, b, c = 100, 200, 300
	print("In A ", a,b,c,d)
	def FunB():
		a, b = 1000, 2000
		print("In B ", a,b,c,d)
		def FunC():
				a = 10000
				print("In C ", a,b,c,d)
		FunC()
	FunB()
FunA()
print("In __main__", a, b, c, d)