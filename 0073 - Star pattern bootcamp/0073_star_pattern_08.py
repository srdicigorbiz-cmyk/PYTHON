r = 6
st = "* "
sp = " "

for i in range(r):
    if i == 0 or i ==r-1:
        print(r*st)
    else:
        print(st+(r+2)*sp+st)
    