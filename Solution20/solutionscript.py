interim_list = []

#appned n integers to a list to be multiplied together later
def append_to_list(n):
	for i in range(n,0,-1):
		interim_list.append(i)


#calculate the factorial from interim list
def calc_factorial():
	result = 1
	for i in range(0, len(interim_list)):
		result = result * interim_list[i]
	print(result)
	return result

#now for the final solution, "listify" the result from calc_factorial and sum the list
def calc_index_sum(n):
	append_to_list(n)
	fact_str = str(calc_factorial())
	index_list = []
	index_sum = 0
	for i in fact_str:
		index_list.append(int(i))
	
	print(index_list)
	index_sum = sum(index_list)

	return index_sum
	

calc_index_sum(100)
