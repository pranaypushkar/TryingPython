#Variable Params
#* defines the variability, params or args are not reserved keywords
def total(*params):
	result = 0
	for value in params:
		result+= value
	return(result)

print(total())
print(total(10, 20, 30, 40, 50))
print(total(10, 20, 30, 400, 500, 600, 7000, 8000, 9000))