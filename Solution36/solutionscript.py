pal_list =[]

#borrowed this function from what I previously wrote for solution 4
def is_palindrome(n):
	if n[0] == 0: 
		return False
	#compare characters at beginning and end
	if n[0:1] == n[len(n)-1:len(n)]:
		n = n[1:len(n)-1]
		#return true if there is only a single character after removing first and last otherwise run again recursively
		return True if len(n) < 2 else is_palindrome(n)
	else:
		return False

#this is fed a decimal based numer, first convert then trim then pass through is_palindrome
def base_conv_palsearch(num):
	binary_rep = bin(num).replace('0b','')
	if is_palindrome(binary_rep) and is_palindrome(str(num)):
		pal_list.append(num)

def control_loop():
	for i in range(1,1000000):
		base_conv_palsearch(i)
	print(pal_list)
	print(sum(pal_list))

control_loop()
