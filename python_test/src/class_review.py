__author__ = 'nancy'

class Myclass(object):
    common=10
    def __init__(self):
        self.myvariable=3
    def myfunction(self,arg1,arg2):
        return self.myvariable

    # this is the class instantiation
classinstance=Myclass()
classinstance2=Myclass()

print(classinstance.myfunction(1,2))
print(classinstance.common)
print(classinstance.common)

# note how we use the class name instead of the instance
Myclass.common=30
print(Myclass.common,classinstance.common,classinstance2.common)

# this will not update the variable on the class,instead it will bind a new object to the old variable name
classinstance.common=10
print(Myclass.common,classinstance.common,classinstance2.common)

Myclass.common=50
# this has not changed,because "common" is now an instance variable
print(Myclass.common,classinstance.common,classinstance2.common)

# this class inherits from Myclass.the example class above inherits from "object",
# which makes it what's called a "new-style class".multiple inheritance is declared as:
# class otherclass(Myclass,Myclass2,MyclassN)

class otherclass(Myclass):
    # the "self" argument is passed automaticall and refers to the class instance,so
    # you can set instance variables as above,but from inside inside the class
    def __init__(self,arg1):
        self.myvariable=3
        print(arg1)

classinstance3=otherclass("hello")
print(classinstance3)
print(classinstance3.myfunction(1,2))

# This class doesn't have a .test member, but
# we can add one to the instance anyway. Note
# that this will only be a member of classinstance3.

classinstance3.test=10
print(classinstance3.test)