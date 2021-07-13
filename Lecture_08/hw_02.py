def succ(A, x):
    M = list()
    W = [x]
    while W:
        u = W.pop()
        M.append(u)
        for v in A[u]:
            if v not in M:
                W.append(v)
    return M

A = { 0: [2], 1: [2], 2: [1,3], 3: [4,5], 4: [4], 5: [] }
print(succ(A, 2))