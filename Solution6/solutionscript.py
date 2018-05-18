#Function for calculating the sum of squares within a given range (1^2 + 2^2 + 3^2 + ... + n^2)
def sum_squares(n):
	sigma = 0
	for i in range(1,n+1):
		sigma += i**2
	return sigma

def square_sum(n):
	sigma = 0
	for i in range(1, n+1):
		sigma += i
	return sigma**2


def sum_sqdiff():
	return square_sum(100) - sum_squares(100)


print(sum_sqdiff())
