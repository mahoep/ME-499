#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''
import numpy as np
from complex import Complex, sqrt
from roots import *
import random

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

    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Addition Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)
        a = Complex(re, im) + num
        b = complex(re, im) + num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()
        a = Complex(re, im) + num
        b = complex(re, im) + num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        a = Complex(re1, im1) + Complex(re2, im2)
        b = complex(re1, im1) + complex(re2, im2)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

    return 'Number of times integer addition resulted in a difference: {} \n\
Number of times float addition resulted in a difference: {} \n\
Number of times complex addition resulted in a difference: {}'\
        .format(int_fail, float_fail, complex_fail)

def radd_check():

    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Right Addition Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)
        a = num + Complex(re, im)
        b = num + complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()
        a = num + Complex(re, im)
        b = num + complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        a = Complex(re2, im2) + Complex(re1, im1)
        b = complex(re2, im2) + complex(re1, im1)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

    return 'Number of times right integer addition resulted in a difference: {} \n\
Number of times right float addition resulted in a difference: {} \n\
Number of times right complex addition resulted in a difference: {}'\
        .format(int_fail, float_fail, complex_fail)

def sub_check():

    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Subtraction Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)
        a = Complex(re, im) - num
        b = complex(re, im) - num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()
        a = Complex(re, im) - num
        b = complex(re, im) - num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        a = Complex(re1, im1) - Complex(re2, im2)
        b = complex(re1, im1) - complex(re2, im2)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

        return 'Number of times integer subtraction resulted in a difference: {} \n\
Number of times float subtraction resulted in a difference: {} \n\
Number of times complex subtraction resulted in a difference: {}'\
.format(int_fail, float_fail, complex_fail)

def rsub_check():

    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Right Subtraction Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)
        a = num - Complex(re, im)
        b = num - complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()
        a = num - Complex(re, im)
        b = num - complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        a = Complex(re2, im2) - Complex(re1, im1)
        b = complex(re2, im2) - complex(re1, im1)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

        return 'Number of times right integer subtraction resulted in a difference: {} \n\
Number of times right float subtraction resulted in a difference: {} \n\
Number of times right complex subtraction resulted in a difference: {}'\
.format(int_fail, float_fail, complex_fail)

def mul_check():

    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Multiplication Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)
        a = Complex(re, im) * num
        b = complex(re, im) * num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()
        a = Complex(re, im) * num
        b = complex(re, im) * num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        a = Complex(re1, im1) * Complex(re2, im2)
        b = complex(re1, im1) * complex(re2, im2)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

        return 'Number of times integer multiplication resulted in a difference: {} \n\
Number of times float multiplication resulted in a difference: {} \n\
Number of times complex multiplication resulted in a difference: {}' \
.format(int_fail, float_fail, complex_fail)

def rmul_check():

    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Right Multiplication Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)
        a = num * Complex(re, im)
        b = num * complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()
        a = num * Complex(re, im)
        b = num * complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        a = Complex(re2, im2) * Complex(re1, im1)
        b = complex(re2, im2) * complex(re1, im1)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

        return 'Number of times right integer multiplication resulted in a difference: {} \n\
Number of times right float multiplication resulted in a difference: {} \n\
Number of times right complex multiplication resulted in a difference: {}'\
.format(int_fail, float_fail, complex_fail)

if __name__ == '__main__':
    #construct()
    #string_return()
    #parts()
    print(add_check(), '\n')
    print(radd_check(), '\n')
    print(sub_check(), '\n')
    print(rsub_check(), '\n')
    print(mul_check(), '\n')
    print(rmul_check(), '\n')

