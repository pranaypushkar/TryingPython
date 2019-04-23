#!/usr/bin/python

RateOfInterest = 5
def Calc(P,T):
	global RateOfInterest
	RateOfInterest = 6
	print(P*T*RateOfInterest/100)
	
Calc(100000, 1)
print(RateOfInterest)