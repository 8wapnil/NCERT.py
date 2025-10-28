names = ["Neena", "Meeta", "Geeta", "Reeta", "Seeta"]

for i in range(4):
   min_index = i
   for j in range(i + 1, 5):
	   if names[j] < names[min_index]:
		   min_index = j
   names[i]names[min_index] = names[min_index], names[i]

print(names)