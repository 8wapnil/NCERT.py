with open("swapnil.log") as log:
	for i in reversed(log.readlines()): print(i.strip())