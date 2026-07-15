#upper butterfly
r = 9
c = 9
st = "* "
sp = " "

for i in range(1,r+1,2):
    print(i*sp+((r-i+1)*st))

for i in range(3,r+1,2):
    print((r-i+1)*sp + i*st)

