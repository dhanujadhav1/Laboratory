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










