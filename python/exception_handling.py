# try and except 

# two things can be done when we catch exception 
# 1) catch raised exception  in formation in except block - 
# once exceeption is caught, we can either perform graceful exit or rectify the exceptional situation and continue execution.
# 2) Raise the exception further - Default exception handler catches the object print s stack trace and terminates.

# try block - enclose in it the code that you anticipate will cause an exception.
# Except block - catch the raised exception in it.

try :
    a=int(input("Enter an integer:"))
    b=int(input("Enter an integer:"))
    c=a/b
    print("c=",c)
except ZeroDivisionError:
    print("Denominator is zero")

# When no exception occures while executing try block control goas to first line beyond the except block
# and if exception occures during execution of statements in try block an exception is raised and rest of the try block is skipped 
# after except  control goas to the next line after except block

try : 
    # some statement 
    pass
except(NameError,TypeError,ZeroDivisionError):
    pass

# or 

try:
    # some statement 
    pass
except(NameError):
    print("Name Error")
except(ValueError):
    print("Unable to convert string into int")
except:
    print("Some unknown error")
# In above it tries to match exception and execute perticular except block 

# user- defined exceptions

# else block (optional)
# if else block is present in try except block then it is executed if no exception occurs during execution of the try block
# and it is written after all except blocks
try:
    pass
except:
    pass
else:
    pass

# finally block 
# this block is optional - code in this block always runs no matter what. Even if return or break occures first.
# It is placed after except block (if exist)
# try block must have except block and/or finally block
# this block is used for releasing external resources like databse connections, network connections.
