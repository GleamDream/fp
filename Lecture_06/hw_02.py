def concat(L):
	ret = 0
	for x in L:
		ret += x
	return ret

print(concat([i for i in range(10)]))
