import sys
from solution import firstRepeated

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = firstRepeated(arr)
print(r)
