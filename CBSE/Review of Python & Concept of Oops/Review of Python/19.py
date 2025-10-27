	from datetime import datetime
while True:
	t1 = input("Enter time: ")
	t2 = input("Enter another time: ")
	print(datetime.strptime(t2,"%H:%M:%S") - datetime.strptime(t1,"%H:%M:%S"))