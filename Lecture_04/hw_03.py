import sys
sys.setrecursionlimit(int(1e8))

def f(x):
	return x ** 2 - 2

def bisection(a, b):
	c = (a + b) / 2
	if abs(a - b) > 1e-8:
		if f(a) * f(c) <= 0:
			return bisection(a, c)
		else:
			return bisection(c, b)
	else:
		return c

print(bisection(0, 3))
