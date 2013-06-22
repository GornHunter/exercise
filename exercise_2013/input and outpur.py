__author__ = 'Nancy'

s='Hello,world'
# print(s)
# print(str(s))
# print(repr(s))
# print(str(1/7))
# print(1/7)

x = 10 * 3.25
y = 200 * 200
# s = 'The value of x is ' + repr(x) + ',and y is ' + repr(y) + '...'
# r='The value of x is '+str(x) + ', and y is '+str(y) + '...'
# print(s)
# print(r)
# print(eval(repr(s)))

# hello='hello,world\n'
# hellos=repr(hello)
# he=str(hello)
# print(hellos)
# print(he)

# /$$$$$$$$$$$$$$
# print(repr((x,y,('spam','eggs')))

# for x in range(1,11):
#     print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))

# for x in range(1,11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
#
# print('12'.zfill(5))
# print('-3.14'.zfill(7) )
# print('3.1415926'.zfill(5))

# print('We are the {} who say "{}!"'.format('knights','Ni'))
# print('{0} and {1}'.format('spam','eggs'))
# print("{1} and {0}".format('spam','eggs'))

# print("{food} is {tasted}".format(food='bread',tasted='delicious'))

# table = {'Sjoerd':4127,'Jack':4098,'Dcab':7678}
# for name,phone in table.items():
#     print('{0:10} ==>{1:10d}'.format(name,phone))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# table = {'Sjoerd':4127,'Jack':4098,'Dcab':8637678}
# print('Jack:{0[Jack]:d};Sjoerd:{0[Sjoerd]:d};'
#       'Dcab:{0[Dcab]:d}'.format(table))

# import math
# print('The value of PI is approximately %5.3f.' % math.pi)

f=open('D:/workfile','w+')
f.write('This is a test\n')
f.write('successful\n')
f.write('I love you')

# f.flush()
f.seek(0)
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
#
# for line in f:
#     print(line,end='')

# print(f.readlines())

# print(list(f))

# print(f.write('This is a test\n'))

# f.close()
#
# value = ('the answer',42)
# s=str(value)
# print(f.write(s))

# print(f.read())
# f.close()
# print(f.read())

# with open('workfle','r') as f:



f = open('workfile', 'r')
try:
    all_data = f.read()
finally:
    f.close()

with open('workfile', 'r') as f:
    all_data = f.read()







