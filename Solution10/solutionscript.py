import sympy

#quick 'n dirty

prime_range = sympy.primerange(1,2000000)
prime_list = list(prime_range)


print(sum(prime_list))
