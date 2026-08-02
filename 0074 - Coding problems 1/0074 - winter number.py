# winter number
n_inp = int(input())
n_str = input()
nums = n_str.split()

result = []

for n in nums:
    if n == n[::-1]:
        result.append("YES")
    elif "0" in n:
        result.append("NO")
    else:
        div_res = []
        for x in n:
            if int(n)%int(x)!=0:
                div_res.append("NO")
            else:
                div_res.append("YES")
                
        if "NO" in div_res:
            result.append("NO")
        else:
            result.append("YES")

print(" ".join(result))