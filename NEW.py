n= 4567
def convert(n):
    # Write code here
    result=[]
    rest = n
    while rest > 0:
        result.append(rest % 10)
        rest = rest //10
    


    




    return result

print(convert(n))