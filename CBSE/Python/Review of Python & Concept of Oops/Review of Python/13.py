while True:
	x = int(input("Enter a number: "))
	x = -x if x<0 else x

	for i in range(2, x+1):
		iAmPrime = True

		for j in range(2, i):
			if i%j == 0:
				iAmPrime = False
				break

		if iAmPrime: print(i)