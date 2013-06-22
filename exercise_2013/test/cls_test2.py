__author__ = 'Nancy'

import math


class Rectangle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(a,b)

    def area(self):
        c = self.a * self.b
        print(c)

    def girth(self):
        l = 2 * (self.a + self.b)
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
    t1.area()
    t1.girth()

    print('---------------------')

    s1=Circle(2)
    s1.area()
    s1.girth()