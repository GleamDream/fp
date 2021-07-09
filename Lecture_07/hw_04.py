def merge(L1, L2):
    ret = list()
    while L1 and L2:
        if L1[0] < L2[0]:
            ret.append(L1[0])
            del L1[0]
        else:
            ret.append(L2[0])
            del L2[0]
    ret.extend(L1)
    ret.extend(L2)
    return ret

def msort(L):
    n = len(L)
    if n <= 1:
        return L
    else:
        return merge(msort(L[: n // 2]), msort(L[n // 2:]))

def qsort(L):
    if L == []:
        return []
    else:
        x = L[0]
        del L[0]
        return qsort([y for y in L if y <= x]) + [x] + qsort([y for y in L if y >  x])

def bsort(L):
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

from time import time
from random import randint

def measure(f, L):
    start = time()
    f(L)
    print(time() - start)

L = [randint(0, 100000) for _ in range(10000)]
measure(msort, L.copy())
measure(qsort, L.copy())
measure(bsort, L.copy())