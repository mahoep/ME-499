#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import math

class Complex:
    def __init__(self, re=0, im=0):
        if isinstance(re, int) or isinstance(re, float):
            self.re = re
        else:
            raise TypeError('Real part must be an integer or float')

        if isinstance(im, int) or isinstance(im, float):
            self.im = im
        else:
            raise TypeError('Imaginary part must be an integer or float')

    def __repr__(self):
        return self.__str__()

    def __str__(self, re=0, im=0):
        if self.im < 0:
            r = '({} - {}i)'.format(self.re, abs(self.im))
        else:
            r = '({} + {}i)'.format(self.re, self.im)
        return r

    def __add__(self, other):
        try:
            re = self.re + other.re
            im = self.im + other.im
        except:
            re = self.re + other
            im = self.im

        return Complex(re, im)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            re = self.re - other.re
            im = self.im - other.im
        except:
            re = self.re - other
            im = self.im

        return Complex(re, im)

    def __rsub__(self, other):
        try:
            re = other.re - self.re
            im = other.im - self.im
        except:
            re = other - self.re
            im = -self.im

        return Complex(re, im)

    def __mul__(self, other):
        try:
            re = self.re * other.re - (self.im * other.im)
            im = self.im * other.re + self.re * other.im
        except:
            re = self.re * other
            im = self.im * other

        return Complex(re, im)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        try:
            re = (self.re * other.re + self.im * other.im) / (other.re**2 + other.im**2)
            im = (self.im * other.re - self.re * other.im) / (other.re**2 + other.im**2)
        except:
            re = self.re/other
            im = self.im/other

        return Complex(re, im)

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            re = (other * self.re) / (self.re**2 + self.im**2)
            im = (-other * self.im) / (self.re**2 + self.im**2)

            return Complex(re, im)
        else:
            return self.__truediv__(other)

    def __neg__(self):
        re = self.re * -1
        im = self.im * -1

        return Complex(re, im)

    def __invert__(self):
        re = self.re
        im = self.im * -1

        return Complex(re, im)

    def __pow__(self, power):
        r = sqrt(self.re**2 + self.im**2)
        theta = math.atan2(self.im, self.re)
        real = r ** power * math.cos(power * theta)
        imaginary = r ** power * math.sin(power * theta)

        return Complex(real, imaginary)


def sqrt(num):

    if isinstance(num, int) or isinstance(num, float):
        if num >= 0:
            return num ** (1/2)
        else:
            imaginary_ans = abs(num) ** (1/2)
            return Complex(0, imaginary_ans)
            # return imaginary_ans

    elif isinstance(num, Complex) and num.im == 0 and num.re >= 0:
        try:
            return Complex(sqrt(abs(num.re)), num.im)
        except:
            return num

    elif isinstance(num, Complex) and num.re < 0 and num.im == 0:
        return Complex(0, sqrt(abs(num.re)))

    elif isinstance(num, Complex) and num.re == 0:
        re = num.re
        im = num.im

        real_ans = (1 / sqrt(2)) * abs(sqrt(sqrt(re ** 2 + im ** 2) + re))
        if im < 0:
            sign = -1
        elif im == 0:
            sign = 0
        else:
            sign = 1
        imaginary_ans = (sign / sqrt(2)) * abs(sqrt(sqrt(re ** 2 + im ** 2) - re))

        return Complex(real_ans, imaginary_ans)


    elif isinstance(num, Complex) and num.im != 0 and num.re != 0:
        re = num.re
        im = num.im

        real_ans = (1/sqrt(2)) * abs(sqrt(sqrt(re**2 + im**2) + re))
        if im < 0:
            sign = -1
        elif im == 0:
            sign = 0
        else:
            sign = 1
        imaginary_ans = (sign/sqrt(2)) * abs(sqrt(sqrt(re**2 + im**2) - re))

        return Complex(real_ans, imaginary_ans)

    else:
        raise TypeError('Input must be a int, float, or complex')



if __name__ == '__main__':
    a = Complex(1, 2)
    print (-a,'(-1 - 2i)')
    print (~a,'(1 - 2i)')
    a = 1.23
    c = Complex(1.23, 3.45)
    print(sqrt(a), sqrt(c))

