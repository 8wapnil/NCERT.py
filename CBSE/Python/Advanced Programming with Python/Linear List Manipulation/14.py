l = (10, 5, 55, 13, 3, 49, 36)
n = len(l)

print("Bubble sort:")
bs = list(l)
for i in range(n - 1):
	for j in range(n - i - 1):
		if bs[j] > bs[j+1]: bs[j+1], bs[j] = bs[j], bs[j+1]
print(bs)

print("\nIteration sort:")
it = list(l)
for i in range(1, n):
	curr = i
	prev = i - 1
	while prev >= 0 and it[prev] > it[curr]:
		it[prev], it[curr] = it[curr], it[prev]
		curr = curr - 1
		prev = prev - 1
print(it)

print("\nSelection sort:")
ss = list(l)
for i in range(n - 1):
	j = ss.index(min(ss[i:]))
	ss[j], ss[i] = ss[i], ss[j]
	
	if i == 5:
		print(ss)
		break