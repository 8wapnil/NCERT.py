file = open('textfile.txt, 'w')
word = ''
while word.upper()!='END':
	word = raw_input(Enter a word use END to quit)
	if word.upper()!='END': file.write(word +'\n')
file.close()