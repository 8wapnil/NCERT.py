while True:
	uid = "username"
	key = "password"

	username = input("Enter username: ")
	password = input("Enter password: ")

	print("Correct combination!" if username == uid and password == key else "Details don't match")