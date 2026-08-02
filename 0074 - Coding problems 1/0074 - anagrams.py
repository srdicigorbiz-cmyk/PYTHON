inp_no = int(input())

result = 0

for i in range(inp_no):
    num = input()
    inp_list = []
    res_list = []
    inp_list.append(num.split(" "))
    
    
    for r in inp_list:
        for j in r:
            res_list.append("".join(sorted(j)))
            
    
    res_list = [int(x) for x in res_list]
    if res_list[0] == res_list[1]:
        result += 1
   
print(result)