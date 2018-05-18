#pass me str(N)
def is_palindrome(N):
  #compare characters at beginning and end
  if N[0:1] == N[len(N)-1:len(N)]:
	N = N[1:len(N)-1]
	#return true if there is only a single character after removing first and last
	#otherwise run again recursively
	return True if len(N) < 2 else is_palindrome(N)
  else:
	return False


#should return max of the palindrome of products
def find_max3digitpal():
  is_pal = []
  for i in range(99,999):
	for j in range(99,999):
	  if is_palindrome(str(i*j)):
		#unsure if i*j > i-1*j-1 is less expensive than simply printing all to list and returning max
		is_pal.append(i*j)
  print(is_pal)
  print(max(is_pal))

find_max3digitpal()


#Tests								#Desired results
print(is_palindrome(str(4004)))		#true
print(is_palindrome(str(40004)))	#true
print(is_palindrome(str(4404)))		#false
print(is_palindrome(str(4504)))		#false
print(is_palindrome(str(4054)))		#false
print(is_palindrome(str(4005)))		#false
