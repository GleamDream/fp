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

from random import randint
L = [randint(0, 100) for _ in range(100)]
print(L)
print(msort(L))