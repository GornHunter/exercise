__author__ = 'Nancy'

#******************************************************************
# a=[5,4,3,2,1]
# b=['a','b','c','d']
#
# # a.append('a')
# a.extend(b)
# # a.extend(['3ft'])
# # a.insert(0,'family')
# a.insert(6,'china')
# a.insert(6,'8888888')
# # a.remove(8)
# a.remove('china')
# a.insert(2,2)
# # a.remove(2)
# # print(a.count(2))
# # print(a.count(3))
# # print(a.index(2))
# # print(a.index('8888888'))
# a.remove('8888888')
# # a.sort()
# a.reverse()
# print(a.pop(3))
# print(a)
# # print(b)

# ****************************************************************************
# a = [66.25,333,333,1,1234.5]
# # print(a.count(333),a.count(1),a.count('x'))
# a.insert(2,-1)
# a.append(333)
# print(a.index(333))
# a.remove(333)
# a.reverse()
# a.sort()
# print(a)

# *********************************************************************
# stack = [3,4,5]
# stack.append(6)
# stack.append(7)
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack)

# ************************************************************************
# from collections import deque
# d=deque('ghi')
# for elem in d:
#     print(elem.upper())
# d.append('j')
# d.appendleft('f')
# # print(d)
# # print(d.pop())
# # print(d.popleft())
# # print(list(d))
# # print('h' in d)
# # print(d)
# d.extend('jkl')
# print(d)
# d.rotate(1)
# print(d)
# d.rotate(-1)
# print(d)
#
# r=deque(reversed(d))
# print(r)
# r.clear()
# print(r)
# # print(r.pop())
# r.extendleft('abc')
# print(r)

# **********************************************************
# from collections import deque
# queue = deque(['E','J','M'])
# queue.append('T')
# queue.append('G')
# print(queue)
# print(queue.popleft())
# print(queue)
# print(queue.popleft())
# print(queue)

#************************************
def f(x):
    return x % 2 != 0 and x % 3 != 0


a = filter(f, range(2, 25))

print(list(a))


def cube(x): return x * x * x


b = map(cube, range(1, 11))
print(list(b))

