__author__ = 'Nancy'
#
# apple = 1
# if apple:
#     print ("hello")


# word = ('hello' + '4')*5
# print(word)


import functools

def f(n, k):
    if k < 0:
        return 0
    if k == 0:
        return 1

    if k > n:
        return 0

    return f(n - 1, k - 1) + f(n - 1, k)


def generate():
    yhList = []

    for i in range(10):
        if i < 2:
            yhList = [1] * (i + 1)
        else:
            yhList[1:-1] = [tmpNum + yhList[i] for i, tmpNum in enumerate(yhList[1:])]

        t = [str(x) for x in yhList]
        print(i, yhList)
        print(t, "\n", "###".join(t))


generate()

arr = range(10, 20)

t = [(arr[i], tmpNum) for i, tmpNum in enumerate(arr[1:])]
print(t)


def main():
    N = 10
    for i in range(N):
        space = (N - i - 1) * 4 * ' '
        print(space, end="")
        for j in range(i + 1):
            print("%4d    " % f(i, j), end="")
        print()

    a = [1] * 10
    print(a)

    a = list(range(10))
    print(a)

    a[1:2] = [1, 2, 4]
    print(a)

    print(a[4:-1])
    print(a[1:2])

    a = [1, 2, 3, 5]

    bb = [(i, t * t) for i, t in enumerate(a)]

    print(bb)

    print([j for i, j in bb])

    print("; ".join([str(i) for i in a]))

    a = "abc"
    b = "defg"

    print("%s%s%10d" % (a, b, 1))


if __name__ == "__main__":
    pass





    # print()



    # print(f(0, 0), f(1, 0), f(1, 1))

    # print(f(3, 1))
