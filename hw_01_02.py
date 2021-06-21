import sys

def fib_rec(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib_rec(n - 1) + fib_rec(n - 2)

def fib_eq(n):
	return int((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / (5 ** 0.5))

for i in range(8):
	print(fib_rec(i), fib_eq(i))
