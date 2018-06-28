import inflect

def num_to_word():
	pe = inflect.engine()
	#test = pe.number_to_words(1000)
	#print(test)
	#print(len(list(test.replace(' ',''))))
	result = 0
	temp = 0
	interim = []
	for i in range(1,1001):
		temp = pe.number_to_words(i)
		result = result + len(list(temp.replace(' ','').replace('-','')))
	print(result)

num_to_word()
