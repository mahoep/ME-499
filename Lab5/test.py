#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''
import numpy as np
from complex import Complex

def construct():
    try:
        a = Complex(1.0, 2.3)  # 1 + 2.3i
        b = Complex(2)  # 2 + 0i
        c = Complex()  # 0 + 0i
        print('Class construction passed')

    except:
        print('Class construction failed')

def string_return():
    try:
        print('### String Return ###')
        a = Complex(1, 2)
        b = Complex(1, -2)
        print(a)
        print(b)
    except:
        print("Complex number return failed")

def parts():
    try:
        print('### Return real and imaginary parts ###')
        c = Complex(1.2, 3.4)
        print(c.im)
        print(c.re)
    except:
        print("Can not return real or imaginary parts")

def add_check():
    print('### Addition Check ###')
    a = Complex(1, 2)
    b = Complex(3, 4)
    try:
        print(a + b)  # (4 + 6i)
        print(a + 1)  # (2 + 2i)
        print(1 + a)     # (2 + 2i)
    except:
        print('Addition failed')


def sub_check():
    print('### Subtraction Check ###')
    a = Complex(1, 2)
    b = Complex(3, 4)
    try:
        print(a - b)  # -2 -2i
        print(a - 1)  # 0 + 2i
        print(1 - a)  # 0 + 2i
    except:
        print('Subtraction failed')

def mul_check():
    print('### Multiplication Check ###')
    a = Complex(1, 2)
    b = Complex(3, 4)
    try:
        print(a * 2)
        print(2 * a)
        print(-2 * a)
        print(a * b)
        print(b * a)
    except:
        print('Multplication failed')

def div_check():
    print('### Division Check ###')
    a = Complex(1, 2)
    b = Complex(3, 4)
    try:
        print(a / 2)
        print(2 / a)
        print(a / b)
        print(b / a)
    except:
        print('Division failed')

def neg_check():
    print('### Negation Check ###')
    a = Complex(1, 2)
    try:
        print(-a)
    except:
        print('Negation Failed')

def conj_check():
    print('### Complex Conjucate ###')
    a = Complex(1, 2)
    try:
        print(~a)
    except:
        print('Complex Conjucate Failed')

if __name__ == '__main__':
    construct()
    string_return()
    parts()
    add_check()
    div_check()
    neg_check()
    conj_check()
