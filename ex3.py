#!usr/bin/env python3
#-*- coding: utf-8 -*-

# 实例方法
class Student(object):
    '''
    this is a Student class
    '''
    count = 0
    books = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def printInstanceInfo(self):
        print("%s is %d years old" %(self.name, self.age))
    pass
 
wilber = Student("Wilber", 28)
wilber.printInstanceInfo()
