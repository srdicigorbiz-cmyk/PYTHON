print("***CONVERT NUMBER TO LIST OF DIGITS")
n= int(input("Enter number:"))
def convert(n):
    # Write code here
    result=[]
    rest = n
    while rest > 0:
        result.append(rest % 10)
        rest = rest //10
    result = list(reversed(result))
    return result

print(convert(n))