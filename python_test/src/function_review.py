__author__ = 'nancy'


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def f2(kk, a, b):
    return kk(a, b)


def f_return_f(a):
    return lambda x: a * x


k = f_return_f(100)
k(3)

k = f_return_f(-100)
k(3)

f2(minus, 1, 2)
f2(add, 1, 2)


def kkk(map):
    def inner(number):
        map['call_times'] += 1
        return map['first'] + number

    return inner


dictioanry = {'call_times': 0, 'first': 100}

f = kkk(dictioanry)
for i in range(100):
    f(i)
    print(f(i))
print(f(100), dictioanry)

def passing_example(a_list,an_int,a_string="A defualt string"):
    a_list.append("A new item")
    an_int=4
    return a_list,an_int,a_string

my_list=[1,2,3]
my_int=10
print(passing_example(my_list,my_int))
print(my_list)
print(my_int)








