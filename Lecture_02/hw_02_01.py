def reverse(num):
	ret = list()
	for i in range(len(num)):
		ret.append(num[-1 - i])
	return ret

print(reverse([1, 2, 3]))
