import math

def verify_pyth_triplet():
	# I. Structure the for loop to enforce the first Pythagorean requirement a < b < c
	for a in range(1, 1000):
		for b in range(a + 1, 1000):
			csqr = a*a + b*b
			# II. The second requirement c*c = a*a + b*b also checking csqr as a conditional from the preceeding variables saves another nested for loop
			if math.sqrt(csqr).is_integer():
				c = math.sqrt(csqr)
				print('Pyth Triplet found -- (' +str(a)+ '), (' +str(b)+'), (' +str(c)+')' )
				if a + b + c == 1000:
					return a*b*c


print(verify_pyth_triplet())
