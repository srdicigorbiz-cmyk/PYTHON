import sys
from solution import isMinHeap

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = isMinHeap(arr)
print("true" if r else "false")
