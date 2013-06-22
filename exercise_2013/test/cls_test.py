__author__ = 'Nancy'


class A(object):
    a = 1

    def f(self, name):
        print(name, "self.a", self.a)

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("init", a, b)

    def seta(self, var):
        self.a = var * 10


class B(A):
    def f(self, name):
        print("this is B's f func")


if __name__ == '__main__':
    A(1, 2)

    a1 = A(2, 3)
    a2 = A(3, 5)

    # a = 1

    a1.f("a1")
    a2.f("a2")
    a1.seta(100)

    print("-----------------")

    a1.f("a1")
    a2.f("a2")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    b1 = B(7, 0)
    b1.f("b1")



