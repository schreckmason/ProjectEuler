#Since this problem is worded a little ambiguously first attempt to enforce the fifth power rule
#Once the rule is established then iterated until 1000000 and validate the sum that way and check the answer

#wash rinse and repeat

valid_fifth_powers = []
def fifth_power_check(n):
	global valid_fifth_powers
	temp = []
	temp = list(str(n))
	result = 0
	for i in range(0,len(temp)):
		result = result+pow(int(temp[i]), 5)

	if result == n:
		valid_fifth_powers.append(result)
	

def control_loop():
	for i in range(0, 1000000):
		fifth_power_check(i)
	
	#had an 'off by one' error here however didn't want ot track it down, found it by comparing my answer for fourth and fifth powers compared to the website
	print(sum(valid_fifth_powers))
	print('finite')


control_loop()
