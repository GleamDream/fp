def join(L, s):
	ret = ""
	for i in range(len(L) - 1):
		ret += L[i]
		ret += s
	ret += L[-1]
	return ret

print(join(["123", "45", "67"], "ab"))
