__author__ = 'Nancy'

from functools import reduce

#
# # seq=range(8)
# def add(x, y):
#     return x + y
#
# #
# # a=map(add,seq,seq)
# # print(list(a))
#
# b = reduce(add, range(1, 11))
#
#
# print(b)

# def divide(k):
#     return k % 2 == 0
#
#
# def fang(x):
#     return x * x
#
#
# def add(h, j):
#     return h + j
#
#
# a = filter(divide, range(1, 11))
# # print(list(a))       list只能用一次，此处两个print所输出的list(a)不一样。前一个可以输出数字，后一个为空，
# # print(list(a))
#
# b = map(fang, a)
# c=reduce(add,b)
# print(c)
#
# def sum(seq):
#     def add(x,y):return x+y
#     return reduce(add,seq,0)
# print(sum(range(1,11)))
# print(sum([]))

# square=[]
# for x in range(10):
#     square.append(x**2)
# print(square)

# square=[x**2 for x in range(10)]
# print(square)

# square = map(lambda x: x**2,range(10))
# print(list(square))

# a=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(list(a))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#            combs.append((x, y))
# print(list(combs))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
# vec = [-4,-2,0,2,4]
# print([x*2 for x in vec])
# print([x for x in vec if x >= 0])
# print([abs(x) for x in vec])
#
# freshfruit = {'  banana','  loganberry','passion fruit   '}
# print([weapon.strip() for weapon in freshfruit])
#
# print([(x,x**2) for x in range(6)])
# vec=[[1,2,3],[4,5,6],[7,8,9]]
# print([num for elem in vec for num in elem])

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# from math import pi
#
# import math
#
# print([str(round(pi, i)) for i in range(1, 6)])
#
# print(type([round(pi, i) for i in range(1, 6)]))
#
# for i in range(1, 6):
#     print(round(pi, i), math.floor(3.5), math.ceil(3.5))
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%555555
#
# import math
#
# help(math)