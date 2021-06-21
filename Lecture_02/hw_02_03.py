def ascending(num):
	for i in range(len(num) - 1):
		if num[i] > num[i + 1]:
			return False
	return True

print(ascending([2, 4, 7]))
print(ascending([2, 4, 7, 3]))
