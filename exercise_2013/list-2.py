__author__ = 'Nancy'

# for i,v in enumerate(['apple','plant','orange']):
#     print(i,v)

# $$$$$$$$$$$$$$
# questions=['name','quest','favorite color']
# answers = ['jack','the holy grail','blue']
# for q,a in zip(questions,answers):
#     print('what is your {0}? It is {1}').format(q,a)

# for i in reversed(xrange(1,10,2)):
#     print(i)

# b=['eea','byu','ios','desk','eii','ftz','eea']
# for i in sorted(set(b)):
#     print(i)

# knights = {'gallahad':'the pure','robin':'the brave'}
# for k,v in knights.iteritems():
#     print(k,v)
#
# words = ['ad', 'dggjskl', 'whfjk']
# for w in words[:]:
#     if len(w) > 5:
#         # pass
#         words.insert(0, w)
#     print(w)
# print(words)
#
# for i, word in [(0, 'tic'), (1, 'tac'), (2, 'toe')]:
#     print(i, word)
#
# for i, j in zip(range(10), range(10, 20)):
#     print(i, j)
#
# for i, word in zip(range(0, len(words)), words):
#     print(i, word)
#
# for i in reversed(range(1, 10, 2)):
#     pass
#     # print i
#
# $$$$$$$$$$$$$$$$$$$
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(matrix)

print([[row[i] for row in matrix] for i in range(4)])


for i in range(4):
    print("[", end="")
    for row in matrix:
        print(row[i], end=" ")
    print("]")


import math

# math.pow(2, 5)

print("--------------")
print([row for row in matrix])

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)
#
# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)
#
# print(list(zip(*matrix)))

# $$$$$$$$$$$$$$$$$$$$$$$4444444444444
#
# a = [-1,1,66.25,333,333,1234.5]
# print(a)
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)
# del a
# print(a)

# t=12345,54321,'hello!'
# print(t[0])
# print(t)
#
# u=t,(1,2,3,4)
# print(u)
# v=([1,2,3],[4,5,6])
# print(v)

# empty = []
# singleton = 'hello',
# h='hello'
# print(len(empty))
# print(len(singleton))
# print(len(h))
#
# e = [1, 1]
# a = 1
# b = 1
# for i in range(1, 101):
#     # a, b = b, a + b
#     c = b
#     b = a + b
#     a = c
#
#     e.append(b)
# print(e)

# def f(n):
#     if n<=2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
#
# for n in range(10):
#     print(f(n),end=" ")

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         a = i * j
#         print("%d * %d = %d" % (j, i, a), end="      ")
#     print()

# basket = {'apple','orange','apple','pear','orange','banana'}
# print(basket)
#
# print('orange' in basket)
# print('crabgrasss' in basket)

# a=set('abracadabra')
# b=set('alacazam')
# print(a)
# print(b)
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)
#
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)
#
# print((1,2,3) < (1,2,4))
# print([1,2,3] < [1,2,4])
# print('ABC'<'C'<'Pascal'<'Python')
# print('a'<'A')
# print((1,2,3,4) < (1,2,4))
# print((1,2)<(1,2,-1))
# print((1,2,3) == (1.0,2.0,3.0))
# print((1,2,('aa','ab'))<(1,2,('abc','a'),4))

# string1,string2,string3 = '','Trondheim','Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)


