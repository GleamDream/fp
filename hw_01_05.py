def leibniz(n):
	lz = 0
	for i in range(n + 1):
		lz += ((-1) ** i) * (4 / (2 * i + 1))
	return lz

for i in range(100):
	print(leibniz(i))
