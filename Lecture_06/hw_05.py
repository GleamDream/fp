def bsort(L):
	for i in range(len(L) - 1):
		for j in range(i + 1, len(L)):
			if L[i] > L[j]:
				L[i], L[j] = L[j], L[i]

from random import random
L = [int(random() * 10) for _ in range(10)]
print(L)
bsort(L)
print(L)
