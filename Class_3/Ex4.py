#!/usr/bin/python3

class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    # if I want to retur the result in a new variable (not very good, if I want to do this, I
    # should not include it inside the class
    def addTwo(self, x, y):
        a = x.r
        b = x.i
        c = y.r
        d = y.i
        return Complex(r=a + c, i=b + d)

    def add(self, y):
        a = self.r
        b = self.i
        c = y.r
        d = y.i

        self.r = a+c
        self.i = b+d

    def multiply(self, y):
        a = self.r
        b = self.i
        c = y.r
        d = y.i

        self.r = a * c - b * d
        self.i = a * d + b * c

    def __str__(self):
        # if I call 'print(c1)' in def main(), it will print whats inside this function
        return str(self.i) + '+' + str(self.r) + 'i'


def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c2.add(c1)
    print(c2)  # uses the __str__ method in the class


if __name__ == '__main__':
    main()
