#!usr/bin/env python3
# -*- coding: utf-8 -*-

# url = http://python.jobbole.com/82297/

# define a class
class Student(object):
    count = 0 #类属性
    books = []
    def __init__(self, name, age):
        self.name = name # 实例属性
        self.age = age
    pass

#代码中分别展示了对类数据属性和实例数据属性的访问
Student.books.extend(["python", "javascript"])  
print("Student book list: %s" %Student.books)    
# class can add class attribute after class defination
Student.hobbies = ["reading", "jogging", "swimming"]
print("Student hobby list: %s" %Student.hobbies)    
print(dir(Student))
 
#实例化 
wilber = Student("Wilber", 28) 
print("%s is %d years old" %(wilber.name, wilber.age))
# class instance can add new attribute 
# "gender" is the instance attribute only belongs to wilber
wilber.gender = "male" #实例生成以后，可以动态添加实例数据类型，但这些实例类型只属于该实例。
print("%s is %s" %(wilber.name, wilber.gender))
# class instance can access class attribute
print(dir(wilber))
wilber.books.append("C#") #类属性可以被类或者实例修改，注意实例修改类属性后会把修改结果保存在类对象中，并会被下一次实例化对象继承。
print(wilber.books)
 
will = Student("Will", 27) 
print("%s is %d years old" %(will.name, will.age))
# will shares the same class attribute with wilber
# will don't have the "gender" attribute that belongs to wilber
print(dir(will))
print(will.books)
