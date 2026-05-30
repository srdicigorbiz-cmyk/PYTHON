#handling multiple errors
def calculator(n1,n2):
    #your code goes here
    try:
        result = n1 / n2
    except (TypeError, ValueError, ZeroDivisionError) as obj:
        print(obj)
    else:
        print(result)
n1 = int(input("number 1:"))
n2 = int(input("number 2:"))
calculator(n1,n2)

#import sys
import sys

age={
    'Peter':23,
    'Lopez':24,
    'Glenn':27,
    'Jay':29
}
def fetch(key):
    #your code goes here
    try:
        age[key]
    except KeyError as obj:
        print(f"({sys.exc_info()[0]}, KeyError({sys.exc_info()[1]}))")
    else:
        print(age[key])

key = input("Key:")
fetch(key)