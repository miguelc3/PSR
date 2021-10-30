#!/usr/bin/python3

from collections import namedtuple
Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    
    c_real = x.r + y.r
    c_imag = x.i + y.i

    c = (c_real, c_imag)
    return c

def multiplyComplex(x,y):

    x_real = x[0]
    x_imag = x[1]

    y_real = y[0]
    y_imag = y[1]

    c_real = (x[0]*y[0]) - (x[1]*y[1])
    c_imag = (x[0]*y[1]) + (x[1]*y[0])

    c = (c_real, c_imag)

    return c

def printComplex(x):
    c = str(x[0]) + '+' + str(x[1]) + 'i'
    return c


def main():
    c1 = Complex(5, 3)
    c2 = Complex(r=-2, i=7)

    c_add = addComplex(c1, c2)
    print('('+printComplex(c1)+') + ('+printComplex(c2)+')'+' = ('+printComplex(c_add)+')')

    c_mult = multiplyComplex(c1, c2)
    print('('+printComplex(c1)+') * ('+printComplex(c2)+')'+' = ('+printComplex(c_mult)+')')


if __name__ == "__main__":
    main()
