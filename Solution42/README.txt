This is the solution to problem 42 from Project Euler

Steps:
	1. Define a function to calculate the first 10000 triangle numbers, this seemed like a large enough pool of numbers to the conduct the comparisons from the text file
		a. First verify the first 10 matched the values given by the problem then append these triangle numbers to a data storage
	2. Define a function that will compute the 'value' of a string based upon the alphabetical index
		a. This is done by creating a dictionary which will still afford fast execution times since we will know the letter at the time we reference the dictionary
	3. Handle the file I/O in afinal function that will also keep track of the count of words that have a triangle value
