def product(x, y):
	ret = list()
	for _x in x:
		for _y in y:
			ret.append((_x, _y))
	return ret

print(product([1, 2, 3], ["a", "b"]))
