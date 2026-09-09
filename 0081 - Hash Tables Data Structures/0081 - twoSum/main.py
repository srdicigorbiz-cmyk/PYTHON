import sys
from solution import twoSum

data = sys.stdin.read().split('\n')
arr = list(map(int, data[0].split())) if data[0].strip() else []
target = int(data[1])
r = twoSum(arr, target)
print("%d %d" % (r[0], r[1]))
