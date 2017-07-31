#!usr/bin/env python3
# -*- coding: utf-8 -*-

# url = http://python.jobbole.com/82297/

#静态方法
class Student(object):
    '''
    this is a Student class, i want to testify @staticmethod
    '''
    count = 0
    books = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    @staticmethod
    def printClassAttr():
        print(Student.count)
        print(Student.books)
    pass
 
Student.printClassAttr()    
wilber = Student("Wilber", 28)
Student.count = 3
Student.books = ['CCS']
print('Student.printClassAttr()')
Student.printClassAttr()
print('wilber.printClassAttr()')
wilber.printClassAttr()
