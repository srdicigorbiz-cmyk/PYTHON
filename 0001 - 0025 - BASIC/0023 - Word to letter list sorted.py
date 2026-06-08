def sortString(s):
    # Write code here
    w_list= []
    for w in s.strip():
        w_list.append(w)
    w_list.sort()
    return ''.join(w_list)

s = " word"#input("Enter a word:")
print(sortString(s))

