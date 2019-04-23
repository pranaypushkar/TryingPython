day = input("Enter day of week:")

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day =="Friday":
	print("9.00 AM to 6.00PM")
elif day == "Saturday" :
	print("9.00 AM to 1.00PM")
else :
	print("Holiday")