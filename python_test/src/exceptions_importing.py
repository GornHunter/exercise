__author__ = 'nancy'


def some_function():
    try:
        # division by zero raises an exception
        10 / 0
    except ZeroDivisionError:
        print("Oops,invalid")
    else:
        # exception didn't occur,we/re good'
        pass
    finally:
        # this is executed after the code block is run and all exception have been handled,
        # even if a new exception is raised while handling/
        print("we're done with that.")
        return "----"

print(some_function())


# external libraries are used with the import [libname] keyword.you can also use from [libname] import [funcname]
# for individual functions.here is an example:

import _random
from time import clock

d
