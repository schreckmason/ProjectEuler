#create a function to calculate self powers, check against provided, then get the last ten digits of prescribed problems

def base_power():
	result = 0
	for i in range(1,1001):
		result = result + pow(i,i)

	print(result)

base_power()
