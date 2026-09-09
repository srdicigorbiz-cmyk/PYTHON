import sys
from solution import mostFrequent

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = mostFrequent(arr)
print(r)
