r = 5
c = 9

st = "* "
sp = " "

for i in range(r):        
    
    if i == 0:
         print(sp+c*st, end="")
    
    else:
        
        for k in range(c//2+2): 
            if k == 0:
                print(sp, end = "")
            elif k == i+1:
                print(st, end="")
            else:
                print(2*sp, end="")
        
        for j in range(c//2+1):
            if j == 0 and i < r-1:
                print(2*(c//2-i-1)*sp + st, end="")

    print()              


