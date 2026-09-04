import sys
from solution import sumLastN

data = sys.stdin.read().split('\n')
arr = list(map(int, data[0].split())) if data[0].strip() else []
n = int(data[1])
r = sumLastN(arr, n)
print(r)
