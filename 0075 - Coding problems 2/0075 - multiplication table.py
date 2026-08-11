# Write code here
n = 5


for x in range(n+1):
    if x == 0:
        print(1*" ", end = "")
    else:
        print(x, end = "")
    for y in range(n+1):
        if y == 0:
            print(3*" ", end = "")
        else:
            if x == 0:
                print(y,4*" ", end = "")
            else:    
                print((x*y),4*" ", end = "")
    print("")
    