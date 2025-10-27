n = int(input("How many fields will you enter? Ans: "))
n = -n if n<0 else n
nos = {}

for i in range(n):
	name = input("Enter customer name: ")
	nos[name] = input("Enter their phone: ")

while True:
	query = input("Enter customer name to search: ")
	if query in nos: print(nos[query])
	else: print(query, " doesn't exist.")