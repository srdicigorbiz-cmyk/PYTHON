i = "2 32 45 78 64 21 7 65 18 32 88 1 99"
result = int("".join(n[-1] for n in i.split()[:7])) + sum(int(x) for x in i.split()[7:-1])



print(result)
