class date :
	def __init__(self):
		self.dd = 24
		self.mm = 4
		self.yy = 2019
	def display(self):
		print(self.dd, "-", self.mm, "-" ,self.yy)
		
	def monthValidation(self, newDate):
		#Handling of Feb
			#Leap Year condition
		if newDate < 30 and (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))) and self.mm == 2:
			self.dd = newDate
			return self
		elif newDate < 29 and NOT(( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))) and self.mm == 2:
			self.dd = newDate
			return self
		elif newDate < 32:
			self.dd = newDate
			return self
	
		if newDate > 31:
				monthIndex = self.mm - 1
				newDate = newDate - lstDays[monthIndex]
				if(newDate > 27) :
					self.mm = self.mm + 1
					monthValidation(self, newDate)
					self.dd = newDate
		
	def __add__(self, value):
		lstDays = [31, [28, 29], 31, 30, 31, 30, 31, 31 , 30 ,31 ,30 ,31]
	
		newDate = self.dd + value
		
		monthValidation(self, newDate)
		
		return self
			
	
		
today = date()
#print(dir(today))
today.display()
tomorrow = today + 1
#tomorrow = today + 100
#tomorrow.display()


		#self.mm = self.mm + value
		#self.yy = self.yy + value
		 #> 29 AND self.mm == 2
		 
		 
		 
		 
		 #if(newDate < 0):
			#print("Day cannot be negative")
		#if(newDate > 31 ):
		#	pass
			#print("Day cannot be more than 31 or negative")
			#break
			
			
		
