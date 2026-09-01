import sys
from solution import removeDuplicates

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = removeDuplicates(arr)
print(' '.join(str(v) for v in r))
