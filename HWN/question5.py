#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import numpy as np


class Polygon:
    def __init__(self, n, side_len=1):
        self.names = {3: 'Triangle', 4: 'Square', 5: 'Pentagon', 6: 'Hexagon'}

        if n % 1 == 0:
            self.n = n
            self.side_len = side_len
            self.perimeter = 1*side_len
            if n < 3:
                raise TypeError('A polygon has minimum of 3 sides')
        else:
            raise TypeError('n must be a whole number')

    def __str__(self):
        try:
            return self.names[self.n]
        except KeyError:
            return '{}-sided Polygon'.format(self.n)

    def area(self):
        "http://mathworld.wolfram.com/RegularPolygon.html"
        inradius = 0.5 * 1/(np.tan(np.pi/self.n))
        a = self.n * inradius**2 * np.tan(np.pi/self.n)
        return a


if __name__ == '__main__':
    s = Polygon(5.0)
    print(s.area())
    print(s)

    p = Polygon(12)
    print(p)

