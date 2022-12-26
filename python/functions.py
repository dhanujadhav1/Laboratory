
# Function defination
def fun():
    print("Inside Function")

#Inner Function - function inside function 
def fun():
    print("Inside Function")
    def fun2():
        print("Inner Function")
    fun2()

fun2()

# parameters and arguments passed to the function
def i_sum(x,y,z):
    return x+y+z
print(i_sum(1,2,3))
a,b,c=1,2,3
print(i_sum(a,b,c))

# To return multiple values from the function store values in List/ Tuple /Set /Dictionary
# Functions are always called by value not called by reference ie. value of the variables is passed not it's id or reference (memory address)
# Function can retuern different types of data through different return types

# When function reaches a end without executing return statement will always return None.

# Arguments in function-
# 1) Positional Argument - def ex_fun(x,y,z) here arguments must be passed in correct positional order
# while sending positional arguments no of argument passed must match to the no of arguments received.
 
# 2) Keyword Argument - This arguments can be passed out of order. Python interpretor uses keywords( Variable names) to match values passed with the arguments with the arguments used in function defination.
# ex - def Ex_fun(a,b,c):
#           return a+b+c
# ex_fun(b=3,c=56,a=20)  // Function calling 
 
# When calling function by providing positional and keyword arguments, Positional arguments must precede keyword arguments 
# ex - ex_fun(10,a=232,str="DJ")

# Variable length positional arguments  - 
# Used when no of positional arguments are  not fix.
# ex- 
def print_it(*args):
    for arg in args:
        print(arg)
# calling above function and args is of type tuple.
print_it(1,2,2,3,"JAVA")

# Variable length keyword arguments -  Used when no of keyword argument to be passed to a function is not certain
# ex
def print_it_kwd(**kwargs):
        print()
        for (name , value) in kwargs.items():
            print(name ," : ",value)


# Calling 
print_it_kwd(a=2,b=5,c="Technical",d="OMG",p=23.23)

# To use different types of arguments precedence oreder is 
# Positioncal Argumetns -> Variable length positional arguments -> Keyword arguments -> Keyword Arguments -> Varialbe length keyword arguments
# ex- 
def print_it_all(i,j,*args,x,y,**kwargs) :
    pass
print_it_all(10,20,x=20,y=30)
print_it_all( 10,20,100,200,x=30,y=40,a=12.2,b=34,c=90)

# Default value - 
# while defining a function default values can be passed so it gets default value when no value is passed.
# Note - while defining a function default arguments must follow non-default arguments
def fun_default_value(a,b=10,c=70,d=90):
    pass

# Unpacking Arguments - 
def print_unpacking_arguments(a,b,c,d):
    pass

#calling by passing list 
lst=[1,2,3,4]

print_unpacking_arguments(*lst)
# * is used to unpack the list tuple set .
#  ** is used to unpack the dictionary
def print_unpacking_dictionary(name="Sanjay",marks=12):
    print(name , marks)
d={'name':'Anil','marks':50}

print_unpacking_dictionary(*d)  # prints keys
print_unpacking_dictionary(**d) # Print Values







