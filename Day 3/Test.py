
class MGM: 
	def Walk3(self):
		print("Walk Elegantly - MGM")
		print(dir(self))

class MGF: 
	def Walk4(self):
		print("Walk Elegantly - MGF")

class PGM: 
	def Walk6(self):
		print("Walk Elegantly - PGM")

class PGF: 
	def Walk7(self):
		print("Walk Elegantly - PGF")
	def PGFFun():
		print("PGF Fun executed")


class Mom(MGM, MGF): 
	#def __del__(self):
	#	print("Object Mom destroyed")
	#def __init__(self):
	#	print("Object Mom constructed successfully")
	def Walk2(self):
		#print("Walk Elegantly - Mom", id(self))
		print("Walk Elegantly - Mom")
	
class Dad(PGM, PGF):
	def Walk5(self):
		#print("Walk Elegantly - Mom", id(self))
		print("Walk Elegantly - Dad")
	#def Talk(self):
	#	print("Talk - Dad")
		
class Infant(Mom, Dad):
	#'First Class - Python'
	#pass
	#def __del__(self):
	#	print("Object Infant destroyed")
	#def __init__(self):
	#	print("Object Infant constructed successfully")
	def Walk1(self):
		print("Walk Elegantly - Infant")



#Mother = Mom()
#Mother.Walk()
#del(Mother)

Baby = Infant()
MGM.Walk3(Baby)
#Baby.Walk()
#Baby.Talk()
#print("id of Mother is ", id(Mother))


#help(Baby)
#print(dir(Baby))