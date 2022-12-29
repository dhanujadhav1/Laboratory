f= open("D:\Laboratory\python\messages.txt",'w')  #It opens a file if present or if not present then it creates a file. file is opened in writing mode

f.write("This is It")   # Writing to file, writes without new line at the end of sentence 
f.write("This is It2")
f.write("This is It3")
f.write("This is It4")

f.close() #closes file, It is imp to close the file

f=open("D:\Laboratory\python\messages.txt",'r')  #It opens a file if present or if not present then it creates a file. file is opened in reading mode

print(f.read()) # It reads all data present in file
f.close()


# Two ways to write to the file
msg="Bad officials are elected by good people who do not vote"
msgs=["Humpty\n", "Sharma\n","sunil\n","Its okay\n"]

f= open("D:\Laboratory\python\messages.txt",'w') 

f.write(msg)
f.writelines(msgs) #To write data
# To write objects other than string, we need to convert them to strings before writing

tpl=('Ajay',23,123423)

f.write(str(tpl))


f.close()

# Three ways to read data  from the file

f=open("D:\Laboratory\python\messages.txt",'r')

data=f.read() #read entire data of file and return as a string
print(data)
f.close()

f=open("D:\Laboratory\python\messages.txt",'r')

no_of_char=12
data = f.read(no_of_char) # Reads first n characters and return as a string

data =f.readline() # Reads a line and return it as a string
data= f.readlines() #Read all lines in a file and form a list of lines.

# ways to read a file line to line to the end of file
# First way
while True:
    data = f.readline()
    if data == '':
        break
    print(data,end="")

# Second way
for data in f:
    print(data,end="")
f.close()

# File opening modes -
# 'r' - open file to read in textmode
# 'w' - open file to write in textmode
# 'a' - open file to append in textmode
# 'r+' - to read and write in text mode
# 'w+' - to read and write in text mode
# 'a+' - to append and read in text mode
# 'rb' , 'wb','ab','rb+','wb+','ab+'- for binary mode

# if no file opening modes are provided then it is opened in read mode
# while opening a file if file alerady exist then it is overwritten.


# with keyword - with keyword closes the file as soon as its usage is over. It also ensures that file is closed even if exception occures while processing it.
# close file if it is not in use, python garbage collector closes file once object is destroyed

with open('messages.txt','r') as f:
    data = f.read()

# when we are reading a file or writing a file, the next read or write operation is performed from the next character/byte as compared to previous read or write operation
# if f.read(1) then next read function will read data from 2nd character in the file


# when we may wish to move to desired position in a file before reading / writing. This can be done by f.seek() method

# f.seek(offset,reference)
f.seek(512,0) # moves to position 512 from begining of the file
f.seek(0,2) # moves to end of file



# Serialization and deserialization -
# while inserting nos in files we have to convert nos into strings before inserting it into a file.
# to read and write complicated data like tuples,lists. for this json module is used, it converts data into appropriate JSON type before writing data to a file.
# Serialization - to convert python data in appropriate json types.
# Deserialization - It converts JSON type reads from the file into python data.

# Serialize and deserialize a list - 
import json

f=open("sampledata",'w+')
lst = [10,20,30,40,50,60]

json.dump(lst,f) #putting data in file

f.seek(0) #bringing pointer to start of the file

inlst = json.load(f)

print(inlst)
f.close()

# Serialize and deserialize a tuple
f=open("sampledata",'w+')
tpl = ('Ajay',23,24.55)

json.dump(tpl,f)

f.seek(0)

intpl = json.load(f)

print(tuple(tpl))

f.close()

# Serialize and deserialize a dictionary

f=open("D:\Laboratory\python\sampledata",'w+')
dct = {'Anil':24,'Ajay':21,'Nisha':45}

json.dump(dct,f)

f.seek(0)

indct = json.load(f)

print( indct)

f.close()

# converting json data in string

str2 = json.dumps(indct)

# Serilization of user defined types

# File and directory operations - 
# File operations - rename, create, delete, copying, checking if an entry is a file, obtaining statistics of a file
# Directory operations - rename, create, delete, copying, recursion creation, listing a directory 
# Path operations - obtaining absolute and relative path, splitting path elements, joining paths
# '.' represent current directory and '..' represent parent directory 

import os 
import shutil

print (os.name)
print (os.getcwd())
print (os.listdir('..'))

if os.path.exists('mydir'):
    print ("mydir already exist")
else:
    os.mkdir('mydir')

os.chdir('mydir')
os.makedirs('.\\dir1\\dir2\\dir3')

stats_of_file = os.stat('myfile.txt')

print("File size", stats_of_file.st_size)

os.rename('myfile','yourfile')
shutil.copy('yourfile','ourfile')
os.remove('yourfile')

currnt_path = os.path.abspath('.')

os.path.join(currnt_path,'yourfile')

