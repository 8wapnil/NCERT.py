file = open("string.txt", "a+")

while True:
    string = input("Enter a sentence: ")
    if string == "END": break
    else: file.write(string + "\n")

file.seek(0)
print(file.read())
file.close()
