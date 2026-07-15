r = 6
c = 11

st = "*"
sp = " "

for i in range(r):
    if i == 0:
        print(c//2*sp+st, end = "")
    else:
        print((c//2-i)*sp + st + (2*i-1)*sp + st, end= "")
    print()