# An object is called iterable if it is capable of returning its members one at a time.
# Iterator is an object which is used to iterate over an iterable.
# zip() - it receives multiple iterable object and returns an iterator of tuples based on them.

words=['A','Sandeep','DJ','MJ']
numbers = [10,20,30,40]

for ele in zip(words,numbers):
    print(ele[0],ele[1])

for ele in zip(words, numbers):
    print(*ele)

for ele1,ele2 in zip(words, numbers ):
    print(ele1,ele2)

# If interables passed to zip are of different size then it returns an iterator of size of smaller iterable.

a=zip(words,numbers)

print(a)
print(list(a))


# Iterators - 

for ch in "Good Afternoon":
    print(ch)

#above for loop call __iter__()  method of str. This method returns an iterator object. Iterator object has a method __next__() which reurns next item in str container.
# when all items are iterated, next call to __next__() raises a StopIteration exception which tells for loop to terminate.
#
# can call __iter__() and __next__()
lst=[10,20,30,40]
i = lst.__iter__()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())

# Insted of calling __iter__() and __next__() we can call iter() and next()
lst=[10,20,30,40]
i=iter(lst)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# hasattr() - hasattr(s,'__iter__') - it checks if __iter__ is in s object. returns True or False

# user- defined iterators 


# Generators - it is very efficient function which create iterators. They use yield statement instead of return statement
# It remembers state of the function, so next time next() is calledit resumes where it had left off last time.
# It is useful where we need to perform calculations on the go and wants one result at a time
def AvgAdj(data):
    for i in range(0,len(data)-1):
        yield (data[i] +data[i+1]) / 2
lst=[10,20,30,40,50]
for i in AvgAdj(lst):
    print(i)

# like  list  comprehesions, generator expressions are also created and they are enclosed within () brackets.
# It is more efficient than list comprehension. it takes less memory since it generates the next element on demand.

print(sum( n * n * n for n in range(20)))

# exit() - terminates the execution of the program.
exit()

 

