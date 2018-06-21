#have a structure to hold indices
indices = []
#define a function to split a given number into it's indices and append to a lsit
def split_num(n):
	len_n = len(str(n))
	for i in range(0, len_n):
		indices.append(int(str(n)[i]))

#define a function to calculat factorial of a number -- copied from Solution 20
def calc_factorial(n):
	result = 1 
	for j in range(n, 1, -1):
		result  = result * j;
	return result

#define a function to compare the sum of the factorials to the original
def comp(n):
	split_num(n)
	interim_fact_list = []
	for i in range(0, len(indices)):
		interim_fact_list.append(calc_factorial(indices[i]))
	fact_sum = sum(interim_fact_list)
	if n == fact_sum:
		print(indices)
		print(fact_sum)
		return True
	else:
		return False


def control_loop():
	result_list = []
	#result_list.append(comp(145))
	for i in range (3, 1000000):
		#result_list.append(comp(i))
		if comp(i):
			result_list.append(i)
		indices.clear()
	
	print(sum(result_list))

control_loop()

#comp(144)
#indices.clear()
#comp(145)
