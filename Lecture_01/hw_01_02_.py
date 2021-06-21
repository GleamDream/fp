import sys

def fib_eq(n):
	return int((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / (5 ** 0.5))

print(fib_eq(int(sys.argv[1])))
