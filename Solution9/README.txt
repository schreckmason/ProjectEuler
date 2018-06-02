Steps I followed to solve Project Euler number 9

Steps:
	1. create a nested for loop structure from 1 to 1000 with the inner loop starting at one greater than a
	2. DO NOT use a triple nested for loop since c*c can be contrived from simply using the two loops
	3. Depending on how many triples you're looking for avoiding this third loop can save thousands of iterations
	4. lastly since the problem is constrained s.t. a + b + c must equal exactly 1000 simply return when that is the case
