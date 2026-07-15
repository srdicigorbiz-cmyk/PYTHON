#upper butterfly
r = 5
c = 10
st = "* "
sp = " "

for i in range(r,0,-1):
    print((i*st)+2*(c-i*2)*sp+(i*st))
    
for i in range(1,r+1):
    print((i*st)+2*(c-i*2)*sp+(i*st))

