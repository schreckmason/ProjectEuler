power_list = []
def calc_powers():
	global power_list
	temp = 0
	for i in range(2,100):
		for j in range(2,100):
			temp = pow(i,j)
			power_list.append(temp)
#	print(power_list)
		


def calc_digital():
	interim_list = []
	for i in range(0,len(power_list)):
		test = list(str(power_list[i]))
		result = sum(map(int, str(power_list[i])))
		interim_list.append(result)
	print(max(interim_list))
	
calc_powers()
calc_digital()

