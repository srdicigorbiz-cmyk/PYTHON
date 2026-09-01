import sys
from solution import findMiddle

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = findMiddle(arr)
print(r)
