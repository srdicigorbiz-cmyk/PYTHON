import sys
from solution import firstNonRepeating

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = firstNonRepeating(arr)
print(r)
