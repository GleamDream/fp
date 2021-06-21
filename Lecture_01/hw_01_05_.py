from matplotlib import pyplot as plt

def leibniz(n):
	lz = 0
	ret = list()
	for i in range(n + 1):
		lz += ((-1) ** i) * (4 / (2 * i + 1))
		ret.append(lz)
	return lz, ret

lz, ret = leibniz(1000)
plt.plot(ret)
plt.show()
