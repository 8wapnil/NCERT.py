while True:
	no = input("enter employee no: ")
	name = input("name: ")
	basic_pay = input("Enter basic pay: ")

	structure = (
		(0.15, 0.08),
		(0.1, 0.05),
		(0.05, 0.03)
	)

	key = 2
	if  basic_pay > 100000: key = 0
	elif basic_pay > 50000: key = 1

	print("HRA: ",  structure[key][0])
	print("DA": ",  structure[key][1])