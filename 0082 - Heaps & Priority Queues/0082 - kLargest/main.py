import sys
from solution import kLargest

data = sys.stdin.read().split('\n')
arr = list(map(int, data[0].split())) if data[0].strip() else []
k = int(data[1])
r = kLargest(arr, k)
print(" ".join(str(x) for x in r))
