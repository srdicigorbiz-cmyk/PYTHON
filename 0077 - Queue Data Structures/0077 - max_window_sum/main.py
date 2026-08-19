from solution import maxWindowSum
import sys

lines = sys.stdin.read().split("\n")
a = [int(x) for x in lines[0].split()]
k = int(lines[1])
print(maxWindowSum(a, k))
