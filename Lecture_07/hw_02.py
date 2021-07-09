def merge(L1, L2):
    ret = list()
    while L1 and L2:
        print(ret)
        if L1[0] < L2[0]:
            ret.append(L1[0])
            del L1[0]
        else:
            ret.append(L2[0])
            del L2[0]
    ret.extend(L1)
    ret.extend(L2)
    return ret

print(merge([1, 3, 5, 7], [0, 2, 4, 6, 8, 10]))