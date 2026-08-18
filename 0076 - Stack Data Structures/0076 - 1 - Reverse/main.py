from reverse import reverse

line = input()
a = [int(x) for x in line.split()]
result = reverse(a)
for element in result:
    print(element)
