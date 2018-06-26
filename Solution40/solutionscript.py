
result_list = []
def stringify():
	global result_list
	test = ""
	for i in range(1,1000001):
		test  = test+str(i)
		if len(test) > 999999:
			#don't do extraneous work
			break
	
	result_list = list(test)

stringify()

#print(result_list)


def calculate_indices():
	#get specific values at indices given in problem 40
	power_0 = int(result_list[0])
	power_1 = int(result_list[9])
	power_2 = int(result_list[99])
	power_3 = int(result_list[999])
	power_4 = int(result_list[9999])
	power_5 = int(result_list[99999])
	power_6 = int(result_list[999999])

	result = power_0 * power_1 * power_2 * power_3 * power_4 * power_5 * power_6
	print(result)
	return result

calculate_indices()
