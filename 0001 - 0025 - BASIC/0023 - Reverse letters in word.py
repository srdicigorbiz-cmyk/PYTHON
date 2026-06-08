def reverseString(s):
    l = len(s)-1
    r_result = []
    while l>=0:
        r_result.append(s[l])
        l -= 1

    return ''.join(r_result)



s = input("Give me a string:")
print(reverseString(s))