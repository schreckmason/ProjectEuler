This is the solution to projecteuler.net problem 8

Started by having a constant of the 1000 number input then creating an empty list that will store results.

Steps:

	1. Create a way to iterate through the list and split into 13-tuples
	2. Create a loop to calculate the product of a 13-tuple and check the result with the first 13 numbers in the string
	3. Append the product to the result list
	4. To speed things up, check if the 13-tuple has a zero, if it does then do not append it to the list and return nothing
	5. Create an iterator variable in a new funciton 'main' that will iterate over each index while it is less than the length of the input string
	6. Lastly use a built-in Python maximum function to get the maximum value from the list and print it to the terminal



