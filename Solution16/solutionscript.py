#Define this function to computer the power digit sum of 2^n
#def power_digit_sum(n):
        #power_res = pow(2,n)
        #print(list(power_res)



def power_digit_sum(n):
	power_res = pow(2,n)
	digit_str = str(power_res)
	digit_iterable = list(digit_str)
	digit_sum = 0
	for i in range(0,len(digit_iterable)):
		digit_sum = digit_sum + int(digit_iterable[i])

	return digit_sum


print(power_digit_sum(1000))
