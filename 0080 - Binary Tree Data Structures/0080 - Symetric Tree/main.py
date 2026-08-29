from solution import isSymmetric
import sys

s = sys.stdin.readline().rstrip("\n")
print("true" if isSymmetric(s) else "false")
