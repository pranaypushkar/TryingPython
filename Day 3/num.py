num = 1 
while num != -1:
	try:
		num = int(input("Enter the number: "))
	#except KeyboardInterrupt:
	#	print("That was not a number")
	#except:
	#	print("That was not a number")
	#except NameError:
	#	print("That was not a number")
	#except ValueError:
	#	print("That was not a number")
	#raise KeyboardInterrupt
	except Exception as a:
		print("type = ", type(a))
		print("args = ", a.args)
		print("a = ", a)
	finally:
		print("In the cleanup block")
	
		