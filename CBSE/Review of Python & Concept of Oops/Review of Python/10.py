while True:
	x = int(input("Enter any number: "))

	print(1)
	for i in range(2, x):
		if x%i == 0: print(i)
	print(x)