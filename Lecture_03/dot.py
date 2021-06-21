def mul(A, B):
	ret = [[0] * len(B[0]) for _ in range(len(A))]
	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(A[0])):
				ret[i][j] = (A[i][k] * B[k][j] + ret[i][j])
	return ret

A = [[1, 2, 3], [4, 5, 6]]
B = [[10, 20], [30, 40], [50, 60]]
print(mul(A, B))
