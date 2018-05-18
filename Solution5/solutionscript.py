import fractions
#Since the problem is only constrained by the fact that a number must only be divisible by all numbers 1-20, start from 20 and work down to 1
def smallest_mult(N):
	#use fractions.gcd(a,b)
	tmp = 1
	for i in range(1, N):
		tmp = tmp*i / fractions.gcd(tmp, i)
	return tmp
	

def is_even(N):
  if N % 2 == 0:
    return True
  else:
	return False	

print(smallest_mult(20))
