__author__ = 'Nancy'


class Myclass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
       return 'Hello World'

# why can not output 'Hello World?'
if __name__ == "__main__":
    x=Myclass()
    xf=x.f
    while True:
        print(xf())


class complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


if __name__ == "__main__":
    x = complex(3.0, -4.5)
    print(x.r, x.i)
    x.counter=1
    while x.counter<10:
        x.counter=x.counter*2
    print(x.counter)
    del x.counter

