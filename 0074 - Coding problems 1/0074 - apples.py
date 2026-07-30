def apples(a1):
    # Write code here
    res=a1%4
    if res == 0:
        return(res)
    else:
        return(4-res)


print(apples(219))