#First have a function that follows the Collatz sequence rules, that is, if n is even then n+1 = n/2 and if it is odd then n+1 = 3n+1
#verify this rule by using the starting number given

#Start in a for loop then that will comput collatz sequences from different starting numbers, keeping a global data store that will only hold the length of each
#sequence, then after the for loop has started all possible sequences under 1M, obtain the max from the global store



collatz_length = []
interim_list =[]
def compute_next(n):
	global collatz_length
	global interim_list
	if (n%2) != 0:
		n = (3*n)+1
		#print(n)
		interim_list.append(n)
		compute_next(n)
	else:
		n = n /2
		#print(n)
		interim_list.append(n)
		if n < 2:
			#add one to the length of the interm list to take the starting number into account
			collatz_length.append(len(interim_list)+1)
			#clear the interim list -- made this a global var instead of managing locally since I wanted to do this recursively
			interim_list = []
			return
		else:
			compute_next(n)
	


#compute_next(13)
#print(collatz_length)

def control_loop():
	for i in range(12,1000000):
		compute_next(i)
	print(max(collatz_length))
	#Note this addition of 12 comes from starting at the compute_next(12) which is the 0th index of collatz_length
	print(collatz_length.index(max(collatz_length))+12)

control_loop()
