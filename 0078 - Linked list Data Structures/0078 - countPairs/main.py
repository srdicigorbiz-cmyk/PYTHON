import sys
from solution import countPairs

data = sys.stdin.read().split('\n')
arr = list(map(int, data[0].split())) if data[0].strip() else []
n = int(data[1])
r = countPairs(arr, n)
print(r)
