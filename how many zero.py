__author__='Nancy'

def zero(n):
    m=0
    while n%10==0:
        n=n/10
        m=m+1
    print(m)

zero(10000)
# zero(0)
zero(999)
