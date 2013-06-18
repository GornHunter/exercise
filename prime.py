def prime(n):
    list = []
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for i in range(2, 100):
    print(i, prime(i))

    # a =prime(12)
    # print(a)
    # print("%s=%s"%("12","*".join([str(i) for i in a])))

    # for n in range(1,100):
    #     a=prime(n)
    #     print("%s=1*%s"%(n,"*".join([str(i) for i in a])))