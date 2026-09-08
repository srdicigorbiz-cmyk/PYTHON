import sys
from solution import moveToFront

data = sys.stdin.read().split('\n')
arr = list(map(int, data[0].split())) if data[0].strip() else []
n = int(data[1])
r = moveToFront(arr, n)
print(' '.join(str(v) for v in r))
