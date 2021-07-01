def reverse(L):
	for i in range(len(L) // 2):
		L[i], L[- 1 - i] = L[- 1 - i], L[i]

L = [10, 20, 30]
reverse(L)
print(L)
