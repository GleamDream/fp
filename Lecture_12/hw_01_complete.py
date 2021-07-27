class rational:
    def __init__(self, x, y):
        """
        Parameters
        ----------
        x : int
            denominator
        y : int
            numerator
        """
        gcd = self.__gcd(x, y)
        self.d = x // gcd
        self.n = y // gcd
    
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
    
    def __floordiv__(self, other):
        return rational(
            self.d * other.n,
            self.n * other.d
        )

    def __truediv__(self, other):
        return float(self // other)

    @classmethod
    def add(self, r1, r2):
        return r1 + r2
    
    @classmethod
    def mul(self, r1, r2):
        return r1 * r2

    def __str__(self):
        return "{}/{}".format(self.d, self.n)
    
    def __float__(self):
        return self.d / self.n


if __name__ == "__main__":
    r1 = rational(8, 6)
    r2 = rational(5, 2)
    for f in [lambda x: x, float]:
        print("r1 =", f(r1))
        print("r2 =", f(r2))
        print("r1 + r2 =", f(r1 + r2))
        print("r1 * r2 =", f(r1 * r2))
        print("r1 // r2 =", f(r1 // r2))
        print()
    print("r1 / r2 =", r1 / r2)