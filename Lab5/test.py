#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''
import numpy as np
from complex import Complex, sqrt
from roots import *
import random
from cmath import sqrt as mathsqrt

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

def tdiv_check():
    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Division Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)

        while num == 0:
            num = random.randint(-r, r)

        while re == 0 and im == 0:
            re = random.randint(-r, r)
            im = random.randint(-r, r)

        a = Complex(re, im) / num
        b = complex(re, im) / num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()

        while re == 0 and im == 0:
            re = random.randint(-r, r)
            im = random.randint(-r, r)

        a = Complex(re, im) / num
        b = complex(re, im) / num

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        while re2 == 0 and im2 == 0:
            re2 = random.randint(-r, r)
            im2 = random.randint(-r, r)

        a = Complex(re1, im1) / Complex(re2, im2)
        b = complex(re1, im1) / complex(re2, im2)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

    return 'Number of times integer division resulted in a difference: {} \n\
Number of times float division resulted in a difference: {} \n\
Number of times complex division resulted in a difference: {}' \
.format(int_fail, float_fail, complex_fail)

def rtdiv_check():

    tests = 1000
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Right Division Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r)

        while num == 0:
            num = random.randint(-r, r)

        while re == 0 and im == 0:
            re = random.randint(-r, r)
            im = random.randint(-r, r)

        a = num / Complex(re, im)
        b = num / complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            int_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(-r, r) + random.random()

        while re == 0 and im == 0:
            re = random.randint(-r, r)
            im = random.randint(-r, r)

        a = num / Complex(re, im)
        b = num / complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            float_fail += 1

    for i in range(tests):
        re1 = random.randint(-r, r)
        im1 = random.randint(-r, r)
        re2 = random.randint(-r, r)
        im2 = random.randint(-r, r)

        while re1 == 0 and im1 == 0:
            re1 = random.randint(-r, r)
            im1 = random.randint(-r, r)

        a = Complex(re2, im2) / Complex(re1, im1)
        b = complex(re2, im2) / complex(re1, im1)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

    return 'Number of times right integer division resulted in a difference: {} \n\
Number of times right float division resulted in a difference: {} \n\
Number of times right complex division resulted in a difference: {}'\
.format(int_fail, float_fail, complex_fail)

def neg_check():
    tests = 1000
    r = 100
    complex_fail = 0
    print('### Negation Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)

        a = -Complex(re, im)
        b = -complex(re, im)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

    return 'Number of times negation resulted in a difference: {}'.format(complex_fail)

def conj_check():
    tests = 1000
    r = 100
    complex_fail = 0
    print('### Conjugate Check ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)

        a = ~Complex(re, im)
        b = complex(re, im).conjugate()

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1

    return 'Number of times inversion resulted in a difference: {}'.format(complex_fail)

def sqrt_check():
    tests = 100
    r = 100
    int_fail = 0
    float_fail = 0
    complex_fail = 0
    print('### Square Root Checks ({} tests) ###'.format(tests))

    for i in range(tests):
        num = random.randint(-r, r)
        a = sqrt(num)
        b = mathsqrt(num)
        # print(num, a, b)
        if isinstance(a, Complex):
            re_diff = abs(a.re - b.real)
            im_diff = abs(a.im - b.imag)

            if re_diff > 1e-8 or im_diff > 1e-8:
                int_fail += 1
        else:
            diff = abs(a-b)
            if diff > 1e-8:
                int_fail += 1


    for i in range(tests):
        num = random.randint(-r, r) + random.random()
        a = sqrt(num)
        b = mathsqrt(num)
        # print(num, a, b)
        if isinstance(a, Complex):
            re_diff = abs(a.re - b.real)
            im_diff = abs(a.im - b.imag)

            if re_diff > 1e-8 or im_diff > 1e-8:
                float_fail += 1
        else:
            diff = abs(a - b)
            if diff > 1e-8:
                float_fail += 1

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        a = sqrt(Complex(re, im))
        b = mathsqrt(complex(re, im))

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            complex_fail += 1





    return 'Number of times square root of an integer resulted in a difference: {} \n\
Number of times square root of a float resulted in a difference: {} \n\
Number of times square root of a complex resulted in a difference: {}'.format(int_fail, float_fail, complex_fail)

def pow_check():
    tests = 100
    r = 15
    fail = 0

    print('### Power Checks ({} tests) ###'.format(tests))

    for i in range(tests):
        re = random.randint(-r, r)
        im = random.randint(-r, r)
        num = random.randint(0, 5)

        a = pow(Complex(re, im), num)
        b = pow(complex(re, im), num)

        re_diff = abs(a.re - b.real)
        im_diff = abs(a.im - b.imag)

        if re_diff > 1e-8 or im_diff > 1e-8:
            fail += 1
            print(a,b,num)

    return 'Number of times the power of a complex number resulted in a difference: {}'.format(fail)


if __name__ == '__main__':
    for i in range(1):
        #construct()
        #string_return()
        #parts()
        # print(add_check(), '\n')
        # print(radd_check(), '\n')
        # print(sub_check(), '\n')
        # print(rsub_check(), '\n')
        # print(mul_check(), '\n')
        # print(rmul_check(), '\n')
        # print(tdiv_check(), '\n')
        # print(rtdiv_check(), '\n')
        # print(neg_check(), '\n')
        # print(conj_check(), '\n')
        print(sqrt_check(), '\n')
        print(pow_check(), '\n')



