#!usr/bin/env python3
#-*- coding: utf-8 -*-

class Parent(object):
    '''
    parent class
    '''
    numList = []
    def numAdd(self, a, b):
        return a+b
 
class Child(Parent):
    pass
 
c = Child()    
# subclass will inherit attributes from parent class    
Child.numList.extend(range(10))
print(Child.numList)
print("2 + 5 =", c.numAdd(2, 5))
 
# built-in function issubclass() 
print(issubclass(Child, Parent))
print(issubclass(Child, object))
 
# __bases__ can show all the parent classes
print(Child.__bases__)
 
# doc string will not be inherited
print(Parent.__doc__)
print(Child.__doc__)
