def add(x, t):
    if t == []:
        t.extend([[], x, []])
    else:
        [l, y, r] = t
        if x < y:
            add(x, l)
        elif x > y:
            add(x, r)

def left_max(t):
    if t == []:
        return
    [l, y, r] = t
    if r == []:
        if l != []:
            [t[0], t[1], t[2]] = l
        else:
            t.clear()
        return y
    else:
        return left_max(r)

def delete(x, t):
    if t == []:
        return
    [l, y, r] = t
    if x == y:
        if l == [] and r == []:
            t.clear()
        elif l == []:
            [t[0], t[1], t[2]] = r
        elif r == []:
            [t[0], t[1], t[2]] = l
        else:
            t[1] = left_max(l)
    elif x < y:
        delete(x, l)
    else:
        delete(x, r)

t = []
for x in [6, 1, 8, 0, 5, 7, 9, 3, 2, 4]:
    print(t)
    add(x, t)
for x in [5, 1, 8, 0, 7, 9, 4, 2, 3, 6]:
    print(t)
    delete(x, t)
print(t)

from random import sample

L = [i for i in range(10)]
for x in sample(L, 10):
    print(t)
    add(x, t)
for x in sample(L, 10):
    print(t)
    delete(x, t)
print(t)