
number = 2
while (number < 100) :
	initialValue = 2
	flag = 0
	while initialValue < number:
		if number % initialValue == 0:
			toggle = 1
			print ("Not a prime number");
			initialValue += 1
			break
	if flag == 0:
		print ("Prime number");
	number += 1