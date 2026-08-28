from solution import isBalanced
import sys

s = sys.stdin.readline().rstrip("\n")
print("true" if isBalanced(s) else "false")
