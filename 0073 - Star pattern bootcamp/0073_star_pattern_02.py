r= 6
sp= " "
st ="* "


for i in range(1, r+1):
    if i < r:
        print((2*r-2*i)*sp+(i*st))
    else:
        for j in range(1, r+1):
            print((j-1)*2*sp+(r+1-j)*st)
    
            
            
        
    
    
            
   