r = 9
c = 9
st = "* "
sp = " "

for i in range(r):
    
    for j in range(c+1):
        if j == 0:
            print(sp, end="")
        
        elif i == 0 or i == r-1:
            print(st, end = "")
        
        elif j == i+1 or j==r-i:
            print(st, end="")
        
        else:
            if i < r//2+1 and j < c+1-i:
                print(2*sp, end = "")    
            if i > r//2 and i < r and j < i+1:
                print(2*sp, end = "")    
    print()
