#!usr/bin/env python3
# coding:utf-8

#url = http://python.jobbole.com/82297/

class Student(object):
    '''
    this is a Student class
    '''
    count = 0
    books = ['MS']
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

wilber = Student("Wilber", 28)
print() #可打印空行
print('==' * 20) 
print('Student.count',Student.count)
print('wilber.count',wilber.count)
print("Student.count is wilber.count: ", Student.count is wilber.count)
wilber.count = 1    
print("Student.count is wilber.count: ", Student.count is wilber.count)
print('Student.count',Student.count)
print('wilber.count',wilber.count)
print(Student.__dict__)
print(wilber.__dict__)
del wilber.count
print("Student.count is wilber.count: ", Student.count is wilber.count)
 
print('Student.count',Student.count)
print('wilber.count',wilber.count)
 
print('==' * 20) 
wilber.count += 3    
print("Student.count is wilber.count: ", Student.count is wilber.count)
print('Student.count',Student.count)
print('wilber.count',wilber.count)
print(Student.__dict__)
print(wilber.__dict__)
 
del wilber.count
 
print('==' * 20) 
print("Student.books is wilber.books: ", Student.books is wilber.books)
wilber.books = ["C#", "Python"]
print("Student.books is wilber.books: ", Student.books is wilber.books)
print(Student.__dict__)
print(wilber.__dict__)
del wilber.books
print("Student.books is wilber.books: ", Student.books is wilber.books)
 
 
print('==' * 20) 
wilber.books.append("CSS")
wilber2 = Student('Tim',25)
print('Student.books',Student.books)
print('wilber.books',wilber.books)
print('wilber2.books',wilber2.books)
wilber.books.append("ADOBE")
print(Student.books)
print(wilber.books)

print("Student.books is wilber.books: ", Student.books is wilber.books)
print(Student.__dict__)
print(wilber.__dict__)
