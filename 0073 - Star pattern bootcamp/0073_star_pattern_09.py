r = 5
c = 9

st = "* "
sp = " "

for i in range(r):        # i kezeli a sorokat
    
    if i == r-1:
         print(sp+c*st, end="")
    
    else:
        
        for k in range(2*c): # k külön kiszámolja és kirakja a csillagokat/belső szóközöket
            
            if k == c-2*i:
                print((c-2*i)*sp+st+(2*i-1)*sp, end="")
        
        for j in range(c-1):
            if j == 0 and i > 0:
                print((2*i-1)*sp + st, end="")

    print()              # sor végén ugrás a következő sorba


