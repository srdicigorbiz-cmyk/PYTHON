def lcp(a):
    for item in a:
        if a[0][0] != item[0]:
            return ""
    
    new_a = []
    for item in a:
        if len(item)==1:
            return item[0]
        else:
            new_a.append(item[1:])

    return a[0][0] + lcp(new_a)

print(lcp(["somehow", "somewhat", "something", "some"]))
print(lcp(["maximum", "minimum"]))
print(lcp(["llo", "lloon"]))