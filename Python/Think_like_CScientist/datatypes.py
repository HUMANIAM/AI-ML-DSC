"""
primitive data types int, float, bool, str. everything else is an object. play with them 
and understand them is a great fun for your mind.
"""
# is used instead of == when we check if 2 variables refers to the same object
# it may return false if the 2 variable has the same values but refer to different 
# objects l1 = [1, 2, 3] , l2=[1, 2, 3] : l1 == l2 >> true but l1 is l2 false
# s1 = "a", s2="a" s1 and s2 refers to the same object so s1 == s2 and s1 is s2 = true

"""
lists are mutable data type so if you assign reference to anthoer variable any change to this
anthor variable will affect the list what if we want to keep the list as it is and play
with the cloned or copied one.
1- a = [1, 2]; b = [:] # clone a to b
"""
def count_occurrence_of_pattern_in_text(text, pattern):
	count, index = 0, 0
	index = text.find(pattern, index)
	while index != -1 :
		count += 1
		index += 1
		index = text.find(pattern, index)

	return count


def multiplicationTable():
	"""make multiplication table from 1 to 12
	"""
	placeholder = "{0:>5}"
	table = ""
	for i in range(1, 13):
		row = "{0:>2}:".format(i)
		for j in range(1, 13):
			row += placeholder.format(i*j)
				
		row += '\n'

		# if this is the first row make it the header and also as 1 multiplaction table
		if i == 1:
			table += ' '*2 + row[2:] 
			table += ' '*2 + ':' +  '-' * len(row[3:]) + '\n'
		table += row

	print(table)


def is_palindrome(text):
	return (text[::-1] == text)


try:
	assert is_palindrome("anana") 
except:
	print("error")
