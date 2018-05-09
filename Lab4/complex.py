#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

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

        return '({} + {}i)'.format(re, im)

    def __radd__(self, other):
        return self.__add__(other)


if __name__ == '__main__':
    a = Complex(1.0, 2.3)  # 1 + 2.3i
    b = Complex(2)  # 2 + 0i
    c = Complex()  # 0 + 0i

    a = Complex(1, 2)
    b = Complex(1, -2)
    print(a)
    print(b)

    c = Complex(1.2, 3.4)
    print(c.im)
    print(c.re)

    a = Complex(1, 2)
    b = Complex(3, 4)
    print(a + b)  # (4 + 6i)
    print(a + 1)  # (2 + 2i)
    print(1 + a)     # (2 + 2i)