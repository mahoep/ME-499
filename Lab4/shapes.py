#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        return pi * radius * radius

    def diameter(self, radius):
        return 2 * radius

    def perimeter(self, radius):
        return 2 * pi * radius


class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self, length, width):
        return length * width

    def perimeter(self, length, width):
        return 2 * length + 2 * width

if __name__ == '__main__':
    from math import pi
    c = circle(1.2)
    area = c.area(1.2)
    print(area)