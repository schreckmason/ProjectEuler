#Define a global data store that will store unique instances of the power relationship 
#Have a function w/ two inputs that will calculate a^b and between an upper and lower bound

unique_occurence = []

def calculate(lower, upper):
	global unique_occurence
	result = 1
	#since the relationship is lower <= a | b <= upper, then to make inclusive, the for loop must have upper+1
	for i in range(lower, upper+1):
		for j in range(lower, upper+1):
			result = pow(i,j)
			if unique_occurence.count(result) == 0:
				unique_occurence.append(result)
			else:
				continue


calculate(2,100)
print(len(unique_occurence))
