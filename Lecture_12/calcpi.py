def pi(acc = 20):
    dx = 1 / (2 ** acc)
    x, s, c = 0, 0, 1
    while s >= 0:
        s, c = s + c * dx, c - s * dx
        x += dx
    return x

def leibniz(acc = 20):
    lz = 0
    for i in range(2 ** acc + 1):
        lz += ((-1) ** i) * (4 / (2 * i + 1))
    return lz

acc = 20
p = pi(acc)
l = leibniz(acc)
print(p)
print(l)
print(abs(p - l))