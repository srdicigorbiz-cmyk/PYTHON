result = []
vowels = ("a", "o","u","i","e")

while True:
    i = input().lower()
    
    if i == "#":
        break

    
    for n in range(len(i)-1):
        part_res = []
        
        for l in i[n:n+2]:
            if l in vowels:
                part_res.append(l)
        if len(part_res) == 2:
            result.append("".join(part_res))

        

for r in result:
    print(r)
print(len(result))

