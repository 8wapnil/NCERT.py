while True:
	x = input("Enter a number: ")
	sum = 0

	for i in x:
		if i not in "-.": sum+= int(i)

	print(sum)