__author__ = 'Nancy'

ntoc = {1: 'one', 2: 'two', 3: 'three'}

a = 123
c = []
while a != 0:
    b = a % 10
    a = int(a / 10)           #注意函数类型要取整，否则就会是小数
    c.append(b)
# print(c)

c.reverse()
# print(c)

for k in c:
   d = ntoc[k]
   print(k,d)

