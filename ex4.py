#!usr/bin/env python3
# -*- coding: utf-8 -*-

#类方法
class Student(object):
    '''
    this is a Student class
    '''
    count = 0
    books = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    @classmethod
    def printClassInfo(cls): #以类对象本身为参数
        print(cls.__name__)
        print(dir(cls))
    pass
 
Student.printClassInfo()    
wilber = Student("Wilber", 28)
wilber.printClassInfo()
