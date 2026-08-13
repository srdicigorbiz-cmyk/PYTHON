i = 7

for x in range(1,i+1):
    if x==1 or x == i:
        print(1*"%"+(i-2)*"@"+1*"%")
    else:
        print(1*"%"+(i-2)*"."+1*"%")