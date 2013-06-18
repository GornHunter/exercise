__author__ = 'Nancy'


def f1(n):
    print("this is f1", n)
    return n


def f2(n):
    print("this is f2", n)
    f1(n - 1)
    return n


# print(f1(10), f2(100))

# f2(1000)


def f(n):
    if n <= 0:
        return
    print("n=%s" % n)
    f(n - 1)
    f(n - 2)


f(4)
