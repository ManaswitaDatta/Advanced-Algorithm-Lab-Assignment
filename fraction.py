class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)


    def __str__(self):
        return str(self.num)+"/"+str(self.den)


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


def main():
    myfraction = Fraction(3,5)
    print(myfraction)

    f1=Fraction(1,4)
    f2=Fraction(1,2)

    print(f1.__add__(f2))
    print(f1 + f2)

    print(f1.__sub__(f2))
    print(f1 - f2)

    print(f1.__mul__(f2))
    print(f1 * f2)

    print(f1.__truediv__(f2))
    print(f1 / f2)

main()