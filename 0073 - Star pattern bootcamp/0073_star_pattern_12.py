r = 6
c = 11

st = "*"
sp = " "

for i in range(r):
    if i == r-1:
        print(c//2*sp+st, end = "")
    else:
        print(i*sp + st + (c-2*i-2)*sp + st, end= "")
    print()