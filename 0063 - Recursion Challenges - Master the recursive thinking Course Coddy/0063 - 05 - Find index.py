def findIndex(s, c):
    # Write code here
    
    if len(s)==0:
        return -1
    
    if c in s:
        if s[0]==c:
            return 0
        else:
            return 1 + findIndex(s[1:],c)
    else:
        return -1




print(findIndex("test", "s")) # 2
print(findIndex("aaa","a")) # 0
print(findIndex("example","p")) # 4
print(findIndex("","p")) # -1
print(findIndex("example","z")) # -1


