import sys
sys.setrecursionlimit(int(1e8))

def f(x, z):
	return x ** 2 - z

def bisection(a, b, z):
	c = (a + b) / 2
	if abs(a - b) > 1e-8:
		if f(a, z) * f(c, z) <= 0:
			return bisection(a, c, z)
		else:
			return bisection(c, b, z)
	else:
		return c

def root(z):
	return bisection(0, z ** 2 + 1, z)

for i in range(2, 10):
	print("root {} = {:.8f}".format(i, root(i)))
