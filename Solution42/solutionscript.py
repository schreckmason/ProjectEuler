#First make a function to calculate the first 10000 triangle numbers...this should be enough to cover the words from the input file
triangle_numbers = []
def calc_t_nums():
	global triangle_numbers
	#tn = 1/2(n)*(n+1)
	result = 0
	for i in range(1,10001):
		result = (0.5*i)*(i+1)
		triangle_numbers.append(result)

#Then make a function that takes in a string and calculates the alphabetical value of it and compares it to alist of known triangle numbers
#define a data defintion to compare letters to
alphabet_vals = {
"A": 1, "B":2, "C":3, "D":4, "E": 5, "F":6, "G":7, "H":8, "I":9, "J":10,
"K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20,
"U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26
}
def comp_alphabet_val(string_to_calculate):
	global alphabet_vals
	interim_list = list(string_to_calculate)
	result = 0
	for i in range(0, len(interim_list)):
		result = result + alphabet_vals[interim_list[i]]

	if triangle_numbers.count(result) !=0:
		return True
	else:
		return False



#Then make a function to parse the text file and iterate through the words, only incrementing a county by one if there is a match
def file_io():
	fo = open("wordfile.txt","r")
	contents = fo.read()
	print(contents)
	word_list = contents.replace('"','').split(",")
	print(word_list)
	fo.close()
	count = 0
	for i in range(0, len(word_list)):
		if comp_alphabet_val(word_list[i]):
			count = count + 1
		else:
			continue
	print(count)

calc_t_nums()
comp_alphabet_val('SKY')

file_io()
