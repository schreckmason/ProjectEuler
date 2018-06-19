#def calc_fib_rec(n):
#	result = 0
#	if n < 3:
#		result = 1
#	else:
#		result = calc_fib(n-1) + calc_fib(n-2)
#	return result

result_list= []
interim_list = []
def calc_fib_iter(n):
	a,b = 0,1
	for i in range(0,n):
		a,b = b,a+b
	return a

#print(calc_fib_iter(40))

print(len(str(calc_fib_iter(4782))))
