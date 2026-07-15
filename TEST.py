r = 9
c = 9

st = "*"
sp = "."


for i in range(r):
    if i < r // 2 + 1:
        for j in range(c):
            if j == c//2-i or j == c//2+i:
                print(st, end="")
            else:
                if j < c//2+i:
                    print(sp, end = "")
    
    if i > r//2:
        for j in range(c):
            if j==i-r//2 or j==(c-1)-(i-r//2):
                print(st, end="")
            else:
                if j < (c-1)-(i-r//2):
                    print(sp, end= "")
    print()
   