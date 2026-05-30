""" Age will be input to your function 'access'. 
Complete the function which will print 
"Access Denied!" 
and stop function execution if age is less than 18. 
Else, print "Session Created!". 
Use Exception handling Only. Create custom Exception 'AccessError'."""
class AccessError(Exception):
    pass

def access(age):
    try:
        if age<18:
            raise AccessError("Access Denied!")
    except Exception as e:
        print(e)
    else:
        print("Session Created!")


age=int(input("Age:"))
access(age)