#step-1: Creating Exception class
class FiveDivisionError(Exception):
    pass

#step-2: raise an Exception for particular condition
try:
    a = int(input("1st Number:"))
    b = int(input("2nd Number:"))
    if b == 5:
        raise FiveDivisionError("Cannot divide by five")
    div = a/b
    print("Division:",div)
#step-3: Handle Exception using except
except Exception as obj:
    print(obj)