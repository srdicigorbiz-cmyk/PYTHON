import sys
from solution import reverseList

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = reverseList(arr)
print(' '.join(str(v) for v in r))
