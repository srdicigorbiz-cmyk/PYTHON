#upper butterfly
r = 8
c = 11
st = "*"
sp = " "

for i in range(2):
    print((1-i)*sp+
          (3+2*i)*st+
          (3-2*i)*sp+
          (3+2*i)*st)

for i in range(r-2):
    print(i*sp+((c-2*i)*st))