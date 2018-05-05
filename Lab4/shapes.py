#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return pi * self.radius * self.radius

    def diameter(self):
        return 2 * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


if __name__ == '__main__':
    from math import pi
    c = circle(1.2)
    print(c.area())
