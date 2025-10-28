nos = []

while True:
	try:
		nos.append(float(input("Enter a number or press any alphabet  to stop: ")))
	except: break

nos.sort()
try: print("Found at position ", nos.index(float(input("Search..."))) + 1)
except: print("Not found!")