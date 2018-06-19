This is the solution to Project Euler problem 16

Steps
	1. Began by using the built-in power function to get a power of two, making it more portable by allowing the power to be passed as a param
	2. Converted the number that is computed by pow() to a string with the goal of making the string iterable
	3. 'listify' the string to separtae indices
	4. Iterate over the list appending the value of each index to the pre-existing sum
