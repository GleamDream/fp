def derivative(f, x):
	e = 1e-9
	return (f(x + e) - f(x)) / e

def newton(f, x):
	e = 1e-9
	while abs(f(x)) > e:
		x = x - f(x) / derivative(f, x)
	return x

def f(x):
	return x * x - 2

print(newton(f, 10))
