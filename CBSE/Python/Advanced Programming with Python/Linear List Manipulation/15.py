students = []

while True:
	student = input("Enter a student name or enter any number  to stop: ")
	if student.isalpha(): students.append(student)
	else: break
	
for i in range(n - 1):
	j = students.index(min(students[i:]))
	students[j], students[i] = students[i], students[j]