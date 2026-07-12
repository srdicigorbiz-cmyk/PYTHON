r = 7
sp = " "
st = "*"

for i in range(r):
    if i == int(r/2):
        print(int(r/2)*sp+st+int(r/2)*sp)
    elif i < int(r/2):
        print((i*sp+st)+(r-2-2*i)*sp+st+(i*sp))
    elif i > int(r/2):
        print((r-i-1)*sp+st+((((i-(r-i))*sp)+st))+(r-i-1)*sp)


            

    