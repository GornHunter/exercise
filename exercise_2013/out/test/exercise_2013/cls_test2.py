__author__ = 'Nancy'

import math


class Rectangle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(a,b)

    def area(self, a, b):
        c = a * b
        print(c)

    def girth(self, a, b):
        l = 2 * (a + b)
        print(l)


class Circle(Rectangle):
    def __init__(self, r):
        self.r = r

    def area(self):
        c = math.pi * self.r ** 2
        print(c)

    def girth(self):
        l = 2 * self.r * math.pi
        print(l)


if __name__ == "__main__":
    Rectangle(2, 4)
    t1=Rectangle(2,4)
    t1.area(2,4)
    t1.girth(2,4)

    print('---------------------')

    s1=Circle(2)
    s1.area()
    s1.girth()