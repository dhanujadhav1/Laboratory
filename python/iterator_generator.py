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

