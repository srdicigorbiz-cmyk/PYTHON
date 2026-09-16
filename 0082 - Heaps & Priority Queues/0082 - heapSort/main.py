import sys
from solution import heapSort

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = heapSort(arr)
print(" ".join(str(x) for x in r))
