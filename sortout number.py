__author__ = 'Nancy'

a = [1, -3, 2, 9, -11, 4, -9, 8, -1, -2, -2, 10, 9]
b = []
c = []
d = []
for i in a:
    if i < 0:
        b.append(i)
    else:
        c.append(i)
# print(b,c)
d = b + c
print(d)

k = 0
for j in range(len(a)):
    if a[j] < 0:
        a.insert(k, a[j])
        del a[j + 1]
        k = k + 1
    else:
        pass

print(a, "@@@@@@@@@@@@@")


