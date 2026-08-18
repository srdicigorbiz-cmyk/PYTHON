from nse import nse

line = input()
a = [int(x) for x in line.split()]
result = nse(a)
for element in result:
    print(element)
