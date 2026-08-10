# Write code here
a = input()
b = input()
duration = int(input())

group1 = ["808", "809","810"]
group2 = ["705", "706","707"]

if duration <= 30:
    bill = duration * 3
elif duration > 30:
    bill = 90 + (duration-30)*2

if a[0:3] in group1 and b[0:3] in group1:
    bill *= 0.7
elif  a[0:3] in group2 and b[0:3] in group2:
    bill *= 0.7

print(f"${int(bill)}")