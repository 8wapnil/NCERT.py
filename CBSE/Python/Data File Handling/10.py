with open("10.txt", "w+") as f:
	f.write("Hello Swapnil!")
	f.seek(0)
	print(f.read())