while True:
	x = input("Enter any number to check if its arms are strong: ")
	sum = 0

	for i in x: sum += int(i)**len(x)
	print(sum == int(x))