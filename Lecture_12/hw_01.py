class rational:
    def __init__(self, x, y):
        gcd = self.__gcd(x, y)
        self.d = x // gcd # denominator
        self.n = y // gcd # numerator
    
    def __gcd(self, x, y):
        while y > 0:
            x, y = y, x % y
        return x

    def __add__(self, other):
        return rational(
            self.n * other.d + self.d * other.n,
            self.n * other.n
        )
    
    def __mul__(self, other):
        return rational(
            self.d * other.d,
            self.n * other.n
        )
    
    @staticmethod
    def add(r1, r2):
        return r1 + r2
    
    @staticmethod
    def mul(r1, r2):
        return r1 * r2

    def __str__(self):
        return "{}/{}".format(self.d, self.n)

if __name__ == "__main__":
    r1 = rational(8, 6)
    r2 = rational(5, 2)
    print("r1 =", r1)
    print("r2 =", r2)
    print("r1 + r2 =", r1 + r2)
    print("r1 * r2 =", r1 * r2)
    print("add(r1, r2) =", rational.add(r1, r2))
    print("mul(r1, r2) =", rational.mul(r1, r2))