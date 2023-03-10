#1) Functions can be assigned to the variable  adn then called using these variables
def fun():
    print("Hello")

f= fun
f()

# 2) Function can be passed as arguments to function and return from function
def fun(a,b,f):
    f()
def func():
    print("I am right")
f=func

fun(1,2,f)  # function passed a argument

# 3) Function can be built at the execution time the way lists, tuples etc can be.
# Lambda Functions / Anonymous function / inline functions - it does not have name, created by using lambda keyword and built at execution time.
# It can take many no of arguments but can return only one value/argument
# Syntax: lambda arguments : expression
#ex
lambda n: n*n*n   # returns cube of the argument
lambda s: s.trim().upper()

# passing values to lambda function
print((lambda s: s.lstrip().upper())(" Sanju_lp"))

# Callling lambda by creating a variable 
avg = lambda lst : sum(lst) / len(lst)

lst_temp=[1,2,3,4,5]

print(avg(lst_temp))

# Higher order function - a function that can receive other functions as argument or return them

d= { 'Oil':230, 'Clip':30,'Stud':230,'Nut':23}

print( sorted( d.items(), key= lambda kv :kv[1]))



# map() -  It applies a function to each element in a sequence like list and tuple and return a new sequence containing results.
# ex - finding square root of each element of the sequence
# syntax -  map ( fun_to_apply, list_of_inputs)
# It returns a map object 

def fun(n):
    return n*n

lst_temp1 = [1,2,3,4,5,6,7]

m1= map(fun,lst_temp1)

print(list(m1))

import math

m2 = map(math.factorial,lst_temp1)
print(list(m2))

# filter() - A filter operation applies to all the elements of a sequence and a sequence of those elemets for which the function returns true.
# ex - checking whether each element in a list is an alphabet and return a list of alphabet.
# syntax - filter(function_to_apply, list_of_inputs)

def fun(n):
    if n%5==0:
        return True
    else:
        return False

lst1 = [5,10,18,27,25]

f2= filter(fun,lst1)

print(list(f2))

lst2 = ['A','X','Y','3','M','4','D']

f3 = filter(str.isalpha,lst2)

print(list(f3))


#reduce() - a reduce operation performs a rolling computation to sequential pair of values in a sequence and returns the results.
# ex - obtaining a product of a list of integers and returning the product. Concatenating all string in a list and returning the final string
# syntax - reduce(fun_to_apply,list_of_inputs)

def get_sum(x,y):
    return x+y

def get_prod(x,y):
    return x*y

lst3=[2,3,4,5,6]

from functools import reduce
reduce(get_sum,[2,3,4,5,6])

reduce(get_prod,lst3)


# Functional programming using lambda

list(map( lambda a: a+2,[1,2,3]))
list(filter( lambda a: a%2==0,[1,2,3,4,5,6,7,8,9,10]))

temp= reduce( lambda a,b:a+b,lst3)
print(temp)







