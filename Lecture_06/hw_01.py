def mymap(f, L):
	m = list()
	for x in L:
		m.append(f(x))
	return m

print(mymap(lambda x: x ** 2, [i for i in range(6)]))
