# Python:

# Day 08:
# Topic covered: Python OOPs, class and object, init function, Class and instance attributes, methods, Abstraction, Encapsulation, Inheritance, Polymorphism, Dunder Functions

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

# Static method:

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

# property method:
# we use property decorator on any method in the class to use the method as a property.

# example:

class subjects:
    def __init__(self,maths,physics,chemistry):
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        # self.percentage = str((self.maths + self.physics + self.chemistry)/3) +"%"

    @property
    def percentage(self):
        return str((self.maths + self.physics + self.chemistry)/3) + "%"

# Super method:
# it is used to access the methods of parent class.

# example:

class Car:

    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class Toyotacar(Car):

    def __init__(self,name,type):
        super().__init__(type)
        self.name = name

t1 = Toyotacar("fortuner","diesel")
t1.start()
print(t1.name)
print(t1.type)       

# class methods:
# class methods is bound to the class and receives the class as an implicit first argument.

# example:

class Person:
    name = "jivika"

    @classmethod
    def changeName(cls,name):
     cls.name = name

p1 = Person()
p1.changeName("pratham")
print(p1.name)
print(Person.name)        

# 5. Abstraction:
# hiding the unnecessary details of a class and only showing the essential features to the user.

# 6. Encapsulation:
# Wrapping data and functions into a single unit(object).

# 7. inheritance:
# when one class(child) derived the properties of another class(parent).

# There are three types of inheritance:

# 1--single inheritance:
# it has one base case and one derived case.

class Car:
    
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod    
    def stop():
        print("car stopped..")

class Toyotacar(Car):

    def __init__(self,name):
        self.name = name

t1 = Toyotacar("fortuner")
t2 = Toyotacar("prisus")

t1.start()

# 2--multi-level inheritance:
# it has one base one derived case and one sub derived case.

class Car:

    @staticmethod
    def start():
        print("car started")\
        
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):

    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyotacar):

    def __init__(self, type):
        self.type = type

c1 = Fortuner("electric")
c1.start()      

# 3--multiple inheritance:
# it can inherit from many parent classes.

class A:
    vara = "welcome to class A"

class B:
    varb = "welcome to class B"

class C(A,B):
    varc = "welcome to class C"

c = C()
print(c.vara)
print(c.varb)
print(c.varc) 

# 8. Polimorphism :
# when the same operators is allowed to having different meanings according to the context.

class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")

num1 = Complex(1,3)
num1.shownumber()            

num2 = Complex(4,6)
num2.shownumber()

# 9. operators and dunder functions:

# 1-add == __add__
# 2-sub == __sub__
# 3-multiply == __mul___
# 4-division == __truediv___

# example 1:

class Complex:                                         #for addition dunder.
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real    
        newImg = self.imaginary + num2.imaginary
        return Complex(newReal , newImg)
    
num1 = Complex(1,3)
num1.shownumber()            

num2 = Complex(4,6)
num2.shownumber()

num3 = num1 + num2
num3.shownumber

# example 2:

class Complex:                                         #for subtraction dunder.
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")

    def __sub__(self,num2):
        newReal = self.real - num2.real    
        newImg = self.imaginary - num2.imaginary
        return Complex(newReal , newImg)
    
num1 = Complex(1,3)
num1.shownumber()            

num2 = Complex(4,6)
num2.shownumber()

num3 = num1 - num2
num3.shownumber()







 
  
  

