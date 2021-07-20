def integral(f, a, b):
	acc = 2 ** 12
	dx = (b - a) / acc
	ret = (f(a) + f(b)) / 2
	for k in range(1, acc):
		ret += f(a + k * dx)
	ret *= dx
	return ret

import math

def x3(x):
	return x ** 3

def xsinx(x):
	return x * math.sin(x)

print(integral(x3, 3, 9))
print(integral(xsinx, 0, 2 * math.pi))
