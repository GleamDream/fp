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
            self.d * other.n + self.n * other.d,
            self.n * other.n
        )

    def __sub__(self, other):
        return rational(
            self.d * other.n - self.n * other.d,
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

    def __pow__(self, other):
        return float(self) ** float(other)

    def __truediv__(self, other):
        return float(self // other)

    def __iadd__(self, other):
        return self + other
    
    def __isub__(self, other):
        return self - other
    
    def __imul__(self, other):
        return self * other
    
    def __ifloordiv__(self, other):
        return self // other
    
    def __itruediv__(self, other):
        return self / other

    def __eq__(self, other):
        return self.d == other.d and self.n == other.n

    def __ne__(self, other):
        return self.d != other.d or self.n != other.n

    def __lt__(self, other):
        return self.d * other.n < self.n * other.d
    
    def __le__(self, other):
        return self.d * other.n <= self.n * other.d

    def __gt__(self, other):
        return self.d * other.n > self.n * other.d
    
    def __ge__(self, other):
        return self.d * other.n >= self.n * other.d

    def __abs__(self):
        return rational(abs(self.d), abs(self.n))

    @staticmethod
    def add(self, r1, r2):
        return r1 + r2
    
    @staticmethod
    def mul(self, r1, r2):
        return r1 * r2

    def __str__(self):
        return "{}/{}".format(self.d, self.n)

    def __repr__(self):
        return "{}/{} : {}".format(self.d, self.n, float(self))
    
    def __float__(self):
        return self.d / self.n

    @staticmethod
    def pi():
        return rational(5706674932067741, 1816491048114374)

    @staticmethod
    def e():
        return rational(43737870773, 16090263458)


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