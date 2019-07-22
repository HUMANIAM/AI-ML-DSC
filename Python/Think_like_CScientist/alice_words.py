"""
count words in alice book
"""
 
def open_file(fname, permissions = "r"):
 	"""open the file if exist and return the file handler"""
 	try:
 		return open(fname, permissions)
 	except:
 		exit(1)


def writeResults(words_occurrences, file):
	ofh = open_file(file, "w+")
	# write header of results
	placehoder = "{0:<10}{1:<5}\n"
	ofh.write(placehoder.format("word", "count"))
	width = len(placehoder.format("word", "count"))
	ofh.write('-' * width + '\n')
 
 	# write results itself
	for pair in words_occurrences:
		ofh.write(placehoder.format(*pair))

	#close the file
	ofh.close()


def clean_line(line):
	"""replace nonimportant character with space"""
	ignored_chars = "/\\\t.,:'()*&^%$#@!~?;{}<>+-[]\""
	def map_char(c):
		if c in ignored_chars: return ' '
		return c

	return ''.join(list(map(map_char, line)))


def countWords(infile, outfile):
	"""count how many every word in infile occures and store results in outfile"""
	ifh = open_file(infile, "r")
	words_occurrences = {}
	
	for index, line in enumerate(ifh.readlines()):
		if line == '\n' : continue
		line = clean_line(line)
		words = line.split()
		for w in words:
			if w.isdigit() or len(w) == 1: continue
			words_occurrences[w] = words_occurrences.get(w, 0) + 1

	# close file and write results
	ifh.close()

	# sort them first then write them in the outfile
	fn = lambda pair : pair[1]
	sorted_word_occurrences = sorted(words_occurrences.items(), key= fn, reverse = True)
	print(len(sorted_word_occurrences))
	writeResults(sorted_word_occurrences, outfile)


def main():
	infile = "aliceAdventures.txt"
	outfile = "alice_words.txt"
	countWords(infile, outfile)

if __name__ == '__main__':
	main()