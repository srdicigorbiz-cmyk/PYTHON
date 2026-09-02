import sys
from solution import mergeSorted

data = sys.stdin.read().split('\n')
a = list(map(int, data[0].split())) if data[0].strip() else []
b = list(map(int, data[1].split())) if data[1].strip() else []
r = mergeSorted(a, b)
print(' '.join(str(v) for v in r))
