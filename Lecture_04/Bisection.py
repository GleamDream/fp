def f(x):
	return x ** 2 - 2

def bisection(a, b):
	e = 1e-8
	while abs(a - b) > e:
		c = (a + b) / 2
		if f(a) * f(c) <= 0:
			b = c
		else:
			a = c
	return (a + b) / 2

print(bisection(0, 3))
