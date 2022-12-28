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