#i
with open("14.txt", "w") as f: f.write("Neither apple nor pine are in pineapple. Boxing rings are square.\nWriters write, but fingers don't fing. Overlook and oversee are opposites. A house can burn up as it burns down. An alarm goes off by going on.")

#ii
more = "more text of your choice"
with open("14.txt", "a+") as f:
	f.seek(0)
	data = f.read()
	print(data)

	f.write(more)
	
	lines = data.split("\n") + ["\n" + more]
	for i in range(1, len(lines) + 1): print(i, f". {lines[i-1]}")
	
	#iii
	print(more)
	
	#iv
	print(data[10:].split("\n")[1])
	
	#v
	print(lines[int(input("Enter the line number to be read: ")) - 1])