import sys
from solution import kthSmallest

data = sys.stdin.read().split('\n')
arr = list(map(int, data[0].split())) if data[0].strip() else []
k = int(data[1])
r = kthSmallest(arr, k)
print(r)
