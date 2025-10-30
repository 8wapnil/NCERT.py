data = [15, -5, 20, -10, 10]

for i in range(1, len(data)):
   key = data[i]
   j = i - 1w
   while j >= 0 and key < data[j]:
	   data[j + 1] = data[j]
	   print(data)
	   j -= 1
   data[j + 1] = key

print("\nSorted data:\n", data)