#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

        if im < 0:
            r = '{} - {}i'.format(self.re, abs(self.im))
        else:
            r = '{} + {}i'.format(self.re, self.im)
        return print(r)

    def __str__(self, re=0, im=0):
        if self.im < 0:
            r = '({} - {}i)'.format(self.re, abs(self.im))
        else:
            r = '({} + {}i)'.format(self.re, self.im)
        return r

if __name__ == '__main__':
    a = Complex(1.0, 2.3)  # 1 + 2.3i
    b = Complex(2)  # 2 + 0i
    c = Complex()  # 0 + 0i

    a = Complex(1, 2)
    b = Complex(1, -2)
    print(a)
    print(b)