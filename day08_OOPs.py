# Python:

# Day 08:
# Topic covered: Python OOPs, class and object, init function, Class and instance attributes, methods, Abstraction, Encapsulation, Inheritance, Polymorphism, Questions

# 1. Class and Object:

# class is a blueprint for creating an objects.
# syntax:
#   class name:
#       name1 = "karan"
# s1 = student()             # object creation
# print(s1.name)

# Example:

class student:
    name = "jivika kaushik"
s1 = student()
print(s1.name)  

# 2.  __init__ function:

# all classes have a function called __init__ , which is always executed when the object is being initiated . it is also known as constructor.

# syntax:
# class student:
#     def __init__ (self,fullname):             #init function
#         self.name = fullname

# example:

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("good things take time")

s1 = student("jivika kaushik",67)        
print(s1.name,s1.marks)

s2 = student("kshama sharma",78)
print(s2.name,s2.marks)

# 3. class and instance attributes:

# 1-class.attr.  #it means same type of attribute.
# 2-obj.attr.    #it means different types of attribute. #if we have diff type of attribute it is always written as self.name

# 4. Methods:

# methods are the functions that belong to objects.
# syntax:
# class student:
#    def __init__(self,name):
#        self.name = name
# def hello(self):                              #method
#     print("hello",self.name)

# example:

class student:
    def __init__(self,name):
        self.name = name
    def hello(self):                  #method
        print("hello everyone")
s1 = student("jivika")        
s1.hello()      

# example 2:

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is",sum/3)
s1 = student("jivika kaushik",[34,56,78])
s1.average()     

# # Static method:

# methods that dont use the self parameter(work at class level)
# syntax :
# class student:
#    @static method   #decorator
#    def college():
#      print("ABC college")

# example:

class student:
    @staticmethod
    def hello_world():
        print("hello world,i am jivika")
s1 = student()
s1.hello_world()        
  
  
