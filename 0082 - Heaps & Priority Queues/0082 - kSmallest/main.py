import sys
from solution import kSmallest

data = sys.stdin.read().split('\n')
arr = list(map(int, data[0].split())) if data[0].strip() else []
k = int(data[1])
r = kSmallest(arr, k)
print(" ".join(str(x) for x in r))
