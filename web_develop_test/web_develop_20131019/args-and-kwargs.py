__author__ = 'nancy'

my_list = ['a', 'b', 'c', 'd']
# print(list(enumerate(my_list)))


def print_everything(*args):
    print  args, type(args)
    print(list(enumerate(args)))
    for count, thing in enumerate(args):
        print('{0}.{1}'.format(count, thing))


# print_everything('a', 'b', 'c', 'd')


def talbe_things(**kwargs):
    for i,j in kwargs.items():
        print('{0}={1}'.format(i,j))

talbe_things(a='fruit',b='vegetable')

def any_function(required_arg,*args,**kwargs):
    print(required_arg)

    if args:
        print(args)

    if kwargs:
        print(kwargs)

any_function("required argument")
any_function("required argument",1,2,"pos3")
any_function("required argument",1,2,"pos3",keyword1=5,keyword2='apple')