with open('textfile.txt') as file:
	data = file.read().split()
	for i in range(1, len(data)): print(i, f". {data[i]}")