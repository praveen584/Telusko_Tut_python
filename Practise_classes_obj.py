# import subprocess
# import platform

# Class is design or blueprint which contains object as a instance. It also contains variable or attributes for storing data
# and methods or functions for behaviour or properties 

# class Computer():

#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
        
    
#     def config(self):
#         proc = subprocess.check_output("ipconfig").decode('utf-8')
#         print(proc)

#     def sysconfig(self):
#         config = platform.uname()
#         print(list(config))    


# dell = Computer('i5',16)
# hp = Computer('i5',8)

# print(type(dell))
# dell.sysconfig()
# print(type(hp))
# hp.sysconfig()


# class Person():

#     def __init__(self):
#         self.name = 'Tejas' #Instance variable
#         self.age = 28

#     def compare(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False

# c1 = Person()
# c1.age = 30

# c2 = Person()

# if c1.compare(c2):
#     print('They are same')
# else:
#     print('They are different')

# print(c1.name)
# print(c2.name)

# class Car():

#     wheels = 4                  #Class variable    

#     def __init__(self):
#         self.mil = 25           #Instance variable
#         self.brand = 'BMW'      #Instance variable

# c1 = Car()
# c2 = Car()

# # class namespace are shared by class variables and instance namespace are shared by object variable

# Car.wheels = 6

# print(c1.brand,c1.mil,c1.wheels)
# print(c2.brand,c2.mil,c1.wheels)

# Instance methods - Accessor methods and mutators methods
# class methods - works with class variable
# static methods

# class Student():

#     school = 'Model college'

#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3

#     # getter and setter methods
#     def get_m1(self):                           #Accessor methods
#         return self.m1

#     def set_m1(self,value):                     #Mutator methods
#         self.m1 = value

#     @classmethod
#     def getschool(cls):
#         return cls.school

#     @staticmethod
#     def info():
#         print('This is a static method')

# s1 = Student(1,2,3)
# s2 = Student(11,22,33)

# print(s1.avg())
# print(s2.avg())
# print(s1.getschool())
# Student.info()


# Inner class

# class Student():                        # Outer class
    
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()

#     def show(self):
#         print(self.name,self.rollno)
#         self.lap.show()

#     class Laptop():                      # Inner class

#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i5'
#             self.ram = 8

#         def show(self):
#             print(self.brand,self.ram,self.cpu)

# s1 = Student('Tejas',12)
# s2 = Student('Rohit',13)

# s1.show()
# s2.show()

# lap1 = s1.lap
# lap2 = s2.lap
# print(lap1.brand,lap1.cpu,lap1.ram)

# Inheritance
# single inheritance - parent is A and B is child
# Multi level inheritance - here father inherits property of his father and child inherit property of father as well as grandfather
# Multiple Inheritance - Here child inherits property from father and mother respectively

# class A():

#     def feature1(self):
#         print('Feature 1')

#     def feature2(self):
#         print('Feature 2')

# class B():

#     def feature3(self):
#         print('Feature 3')

#     def feature4(self):
#         print('Feature 4')

# class C(A,B):

#     def feature5(self):
#         print('Feature 5')

# a1 = A()
# a1.feature1(),a1.feature2()

# b1 = B()
# b1.feature3()

# c1 = C()
# c1.feature1()


# Constructor Inheritance
# class A():

#     def  __init__(self):
#         print('In __init__ A')
        
#     def feature1(self):
#         print('Feature 1')

#     def feature2(self):
#         print('Feature 2')

# class B():

#     def  __init__(self):
#         print('In __init__ B')


#     def feature1(self):
#         print('Feature 3')

#     def feature4(self):
#         print('Feature 4')

# class C(A,B):

#     def __init__(self):
#         super().__init__()
#         print('In __init__ C')

#     def feat(self):
#         super().feature4()

# a1 = C()
# a1.feature1()
# a1.feat()


# Polymorphism
# Duck typing
# Operator overloading
# Method overloading
# Method overriding

# Duck typing
# class Pycharm():
    
#     def execute(self):
#         print('Compiling')
#         print('Running')

# class Vscode():
    
#     def execute(self):
#         print('Compiling')
#         print('Running')

# class Laptop():

#     def code(self,ide):
#         ide.execute()

# ide = Pycharm()

# lap1 = Laptop()
# lap1.code(ide)

# Operator Overloading
# class Student():

#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2

#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)

#         return s3

#     def __gt__(self,other):
#         s1 = self.m1 + self.m2
#         s2 = other.m1 + other.m2
#         if s1 > s2:
#             return True
#         else:
#             return False

# s1 = Student(1,2)
# s2 = Student(1,2)
# s3 = s1 + s2
# print(s3.m1)

# if s1 > s2:
#     print('s1 wins')
# else:
#     print('s2 wins')


# Method overloading
# class Student():

#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2

#     # Method Overloading
#     def sum(self,a=None,b=None,c=None):
#         s = 0
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
#         elif a!=None and b!=None:
#             s = a+b
#         else:
#             s = a    
#         return s


# s1 = Student(2,2)
# print(s1.sum(4))


# Method Overriding
# class A():

#     def show(self):
#         print('In A show')
    
# class B(A):

#     def show(self):
#         print('In B show')

# a1 = B()
# a1.show()


# Abstract class
from abc import ABC,abstractmethod

# class Computer(ABC):

#     @abstractmethod
#     def process(self):
#         pass 

# class Laptop(Computer):
#     def process(self):
#         print('Running')

# # c1 = Computer()
# l1 = Laptop()
# l1.process()

class Car(ABC):

    def __init__(self,brand,name):
        self.brand = brand
        self.name = name

    @abstractmethod
    def display(self):
        print('This is abstract class')  # TypeError: Can't instantiate abstract class Car with abstract method display

class ElectricVehicle(Car):

    def __init__(self,brand,name,mil):
        super().__init__(brand,name)
        self.mil = mil

    def display(self):
        print(f'{self.brand} brand of model name {self.name} has {self.mil} average')

a = ElectricVehicle('Tesla','EV1',30)
a.display()