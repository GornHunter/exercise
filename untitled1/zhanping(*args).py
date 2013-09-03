__author__ = 'nancy'


def print_everything(*args):
    print list(enumerate(args))
    for count, thing in enumerate(args):
        print '{0}.{1}'.format(count, thing)


def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0}={1}'.format(name, value)


def print_three_things(a, b, c):
    print 'a={0},b={1},c={2}'.format(a, b, c)

def any_function(required_arg,*args,**kwargs):
    print required_arg

    if args:
        print args

    if kwargs:
        print kwargs

any_function("Required Argument")
any_function("Required Argument",1,2,"pos3")
any_function("Required Argument",1,2,"pos3",keyword1=5,keyword2='spam')


mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)

table_things(apple='fruit', cabbage='vegetable')
print_everything('apple', 'banana', 'cabbage')