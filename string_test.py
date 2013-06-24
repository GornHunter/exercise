__author__ = 'Nancy'

# print('C:\some\name')
# print(r'C:\some\name')

# print("""
#     usage:thingy[OPTIONS]
#     -h
#     -H hostname
# """)

#3 times 'un',followed by 'ium'
# print(3*'un'+'ium')
#
# s='py'+'thon'
# print(s)

# prefix = 'py'
# s=prefix+'thon'
# print(s)
#
# text=('Is the clock get down?'
#     'No,It is')
# print(text)
#
# word = 'python'
# print(word[0])
# print(word[5])
#
# print(word[-1])
# print(word[-2])
# print(word[-6])
#
# print(word[0:2])
# print(word[2:5])
#
# print(word[:2]+word[2:])
# print(word[4:4])
# print(word[:4]+word[4:])
# print(word[4:]+word[:4])
#
# print(word[:2])
# print(word[4:])
# print(word[-2:])
#
# print(word[4:42])
# print(word[42:])
#
# print(word)
# print(word[0]=='j')
# print(word[2:]=='py')
# print(word[1]=='y')
#
# g='J'+word[1:]
# print(g)
#
# t=word[:2]+'PY'
# print(t)
#
# s='hskgldjsgrktldh'
# print(len(s))

# squares = [1,2,4,9,16,25]
# print(squares)
#
# print(squares[0])
# print(squares[-1])
# print(squares[-3:])
#
# print(squares[:])
#
# print(squares+[36,49,64,81,100])
# cu=squares[0]=0
# squares.append(435)
# print(cu)
# print(squares)
#
# letter=['a','b','c','d','e','f','g']
# print(letter)
# letter[2:5]=['C','D','E']
# print(letter)
# letter[2:5]=[]
# print(letter)
# letter[:]=[]
# print(letter)
#
# letters=['a','b','c']
# print(len(letters))

# a=['a','b','c']
# n=[1,2,3]
# c=a+n
# d=[a,n]
# print(c)
# print(d)
# print(d[0])
# print(d[0][1])
#
# a,b=0,1
# while b<10:
#     print(b,end=' ')
#     a,b=b,a+b
#
# a,b=0,1
# while b<1000:
#     print(b,end=' ')
#     a,b=b,a+b

def fib(n):
    a,b=0,1
    for i in range(n):
        print(b)
        a,b=b,a+b

print(fib(100))


