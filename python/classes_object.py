num =10

temp=10

num is temp
id(num)
id(temp)


class Employee:

    def __init__(self,n='',a=0,s=0.0) -> None:
        self.name=n
        self.age=a
        self.salary=s


    def __del__(self) :
        print("Deleting object"+str(self))

    def set_data(self,n,a,s):
        self.name=n
        self.age=a
        self.salary=s

    def display_data(self):
        print(self.name,self.age,self.salary)

# Creating object by using constructor
E1 = Employee("Sagar",23,34000)
E2= Employee("Sumit",45,2302030)

# Creating object by setter
E1=Employee()
E1.set_data("DJ",45,98000)
E2=Employee()
E2.set_data("MJ",12,12020)

# calling display data method
E1.display_data()
E2.display_data()

# Deleting python object
E1=None
E2=None

# O/P - Deleting object<__main__.Employee object at 0x0000024CCF1A59D0>

# Class variables and methods - these variables (same state) and methods are shared by all objects
# To decalare class variable we have to prepending it with self
# Class variables do not become part of object of a class
# syntax to access calss variables - classname.varname
# also class methods do not receive self argument
# syntax to access class methods - classname.methodname()
# Class methods are to count how many objects have been created

class Fruit:
    count = 0

    def __init__(self,name='',size=0,color=''):
        self.__name=name
        self.__size= size
        self.__color = color

        Fruit.count += 1 

    def print_count():
        print ( Fruit.count)


f1= Fruit("Apple",12,"red")
f2=Fruit("Orange",123,"orange")

print(Fruit.count)

# vars() - returns the dictionary of attributes and their values and dir() - returns a list of attributes

import math 

print(vars()) # Prints dictionary of current attributes with their values of the current module
print(vars(math))  # Prints  dictionary of attributes with their values of the math module

print(dir()) # prints list of the attributes of current module
print(dir(math)) #Prints list of attributes of math module


# Identifier naming convention-
# variables and functions not belong to classes starts with lowercase alphabet
# class names - start with upper case alphabet
# private identifiers - for the variables which needs to access from same class only - starts with two leading underscores __name,__age,__get_birds()
# protected indetifiers - for the variables/methods which needs to access within the class and from     derived class (Inherence)  - names starts with single underscore - _address, _maintain_height

# Operator Overloading - 
# in below ex + operator is overloaded

class Complex :

    def __init__(self,r=0.0,i=0.0) -> None:
        self.__real=r
        self.__imag=i
    
    def __add__(self,other):
        z=Complex()
        z.__real=self.__real+other.__real
        z.__imag=self.__imag+other.__imag

    def display(self):
        print(self.__real,self.__imag)

# Here + operator is by __add__(self,other) method and same can be done to substract __sub__(self,other)
# There are many other operator overlaoding options are available ex - for multiplication __mul__(self,other) , for less than __it__(self,other)
# 
# Function overloading is not supported in python. It does not throw an error but takes latest defination of the method
# 
# In python every entity is an object 
#

class Bird:
    pass

b=Bird()

b.name="Sarthak" # This attribute is created dynamically in Bird class

print(dir(Bird))

# Inheritance and containership (Composition)
# Containership (composition) - used when two classes have 'has a' relationship ex - college 'has a' professor 
#  Inheritance - used when two classes have a 'like a' relationship ex - Maruti car is like a car

# Containership - ex Department object is contained in an Employee object.

class Department :
    pass
class Employee:
    def set_Employee(self) -> None:
        self.dept = Department()

# Inheritance - A new class called derived class can be created to inherit features of an existing class called base class
# Base class is called super or parent class
# Derived class is called sub class or child class

# Base class
class Index:
    def __init__(self) -> None:
        self.count=0
    def display(self):
        print('count='+str(self._count))
    def incr(self) :
        self._count+=1

# Derived class - 
class NewIndex(Index):
    def __init__(self):
        super().__init__() #calling base class constructor

    def decr(self):
        self.count-=1

i = NewIndex()
i.incr()
i.display()
i.decr()

# In inheritance base class constructor followed by derived class construcotor is called

# var - access it from anywhere in the program 
#  _var - access it only from within the class or it's subclass.
#  __var - access it only within the class
# above is only a convention. it will not through an error but it is bad practice to follow.


# isinstance(O,c) - is used to check whether an object o is an instance of a class c. 
# issubclass(d,b) - is used to check whether class d has been derived from class b.

# The object class - all classes in python are derived from a ready made base class called object.
# 
# Features of inheritance - 
# 1) Inheritance of existing feature
# 2) Supressing an existing feature - to implement this hide base class implementation by defining same method in derived class.
# Extending an existing feature - super().base_class_method()
# 
# Types of inheritance -
# Simple inheritance - class NewIndex is derived from class Index
# class NewIndex(Index):
#       def __init__(self):
#       super().__init__()
# 
# Multi-level Inheritance - class HOD is derived from class Professor which is derived from Persont
# 
# Multiple Inheritance - class HardwareSales derived from two base classes - Product and Sales
# 
#class HardwareSales (Product, Sales):
#   def __init__(self):
#         Product.__init__(self)
#         Sales.__init__(self)

# Diamond problem -  This resutls in ambiguity.
#       Base class
#       ___|___
#      |       |
# Derived1   Derived2
#      |       |
#      |-------|
#          |
#          Der class (derived from above two) 
# 
# 
# 

# Abstract Class -  A class from which object can not be created is called Abstract class
from abc import ABC,abstractmethod  #abc - abstract base classes

class shape(ABC):
    @abstractmethod
    def draw(self):
        pass
class Rectangle:
    def draw(self):
        print("draw rectangle")

















