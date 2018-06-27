This is the solution for problem 14 from Project Euler

Steps: 
	1. First define a function that enforces the Collatz sequence rules
		a. Important note that I did this recursively for a little extra challenge however this slowed down execution time so avoid this if you are lacking in compute power
		b. Essentially if it's even then 3n+1 and append to an interim storage
		c. if odd n/2 and append ot the interim list
			i. if n becomes < 2 then clear the interim_list and append the length to the collatz_length list
	2. Define the control loop function that starts at 12 and runs until 999999
		a. Obtain the index of the max from collatz_length
