For this solution I first began the solution by coming up with an idea to find a middle index to determine when I was done removing the first and last index.
However, it is more elegant and concise to do this recursively, since we only care about whether a string can be boiled down to a single character or two different characters
left after removing first and last. Also at each recursive call the first and last characters are compared if they do not match, fail.

For example:
	input 4005004
	0th iteration: 
		- compare 0 and len - 1 char (4 == 4)
		- remove 0 and len - 1 char (00500)
		- len > 2 so call the function again recursively
	1st iteration:
		- compare 0 and len - 1 char (0 == 0)
		- remove 0 and len - 1 char (050)
		- len > 2 so call the function again recursively
	2nd iteration:
		- compare 0 and len - 1 char (0 == 0)
		- remove 0 and len - 1 char (5)
		- len < 2, return True
		
