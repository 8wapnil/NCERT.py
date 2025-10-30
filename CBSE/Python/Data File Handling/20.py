with open(input("Enter filename: ")) as file:
	for i in file.readlines():
		if "#" in i: print(i)