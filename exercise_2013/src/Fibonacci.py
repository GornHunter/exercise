__author__ = 'Nancy'


def fibonacci1(n):
    a, b = 0, 1
    # result=[]
    i = 1
    while i < n:
        i += 1
        print(b,end=' ')
        a, b = b, a + b
    return b

print(fibonacci1(4))


if __name__ == "__main__":

    print(__name__, "=====")