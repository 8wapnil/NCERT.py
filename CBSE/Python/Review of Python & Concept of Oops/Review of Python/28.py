n = int(input("How many numbers will you enter? Ans: "))
n = -n if n<0 else n

nos = []
for i in range(n):  nos.append(int(input("Enter a number: ")))

while True: print("Found" if int(input("Search... ")) in nos else "Not found.")