c= 11
sp= " "
st ="* "


for i in range(1, c+1):
    
    if 1 <= i < (c):
        if i%2:
            print((c-i)*sp + i*st)
    
    if c == i or c == c+1:
        print((c-i)*sp + i*st)
        
        for j in range(c):
            if j%2:
                print(j*sp, ((c-1)-j)*st)
            
            
        
    
    
            
   