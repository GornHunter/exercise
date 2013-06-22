__author__ = 'Nancy'


class A(object):
    a = 1

    def f(self, name):
        print(name, "f()", self.a)

    def __init__(self):
        print("init")

    def seta(self, var):
        self.a = var * 10


class B(A):
    def f(self, name):
        print("this is B's f func")


if __name__ == '__main__':

    A()

    a1 = A()
    a2 = A()

    # a = 1

    a1.f("a1")
    a2.f("a2")
    a1.seta(100)

    print("-----------------")

    a1.f("a1")
    a2.f("a2")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    b1 = B()
    b1.f("b1")



