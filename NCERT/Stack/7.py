nos = eval(input("Enter a list of numbers:"))
odd = []

for i in nos:
    if i%2 != 0: odd.append(i)

print(odd)

biggest = 0

while odd:
    if biggest < odd[-1]: biggest = odd[-1]
    odd.pop()

print(biggest) 