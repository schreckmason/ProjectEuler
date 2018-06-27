#Begin by reading the file and storing each name into a list then deal with delimiters and stripping any extra characters
#Then sort the names, and use a dictionary to obtain the value for each name, multiplied by the index+1 (to avoid mult by 0) of that name


alphabet_values = {
"A":1, "B":2, "C":3, "D":4, "E":5,
"F":6, "G":7, "H":8, "I":9, "J":10,
"K":11, "L":12, "M":13, "N":14, "O":15,
"P":16, "Q":17, "R":18, "S":19, "T":20,
"U":21, "V":22, "W":23, "X":24, "Y":25,
"Z":26
}
content_list = []

def name_val(input_name):
	char_list = list(input_name)
	name_score = 0
	for i in range(0, len(char_list)):
		name_score = name_score + alphabet_values[char_list[i]]
	return name_score
	#print(name_score)

def file_io():
	global content_list
	fo = open('name_file.txt','r')
	contents = fo.read()
	content_list = contents.replace('"','').split(',')
	content_list.sort()
#	print(content_list)
#	print(content_list.index('COLIN'))
	fo.close()


def name_score():
	total = 0 
	file_io()
	for i in range(0, len(content_list)):
		total = total + name_val(content_list[i]) * (i+1)

	print(total)

name_score()
