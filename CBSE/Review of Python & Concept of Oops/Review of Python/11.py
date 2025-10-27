while True:
	x = input("Enter any number to check if its arms are strong: ")
	sum = 0

	for i in x: sum += int(i)**len(x)
	print("It is an Armstrong." if sum == int(x) else "It is not an Armstrong")