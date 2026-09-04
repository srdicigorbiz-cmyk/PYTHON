import sys
from solution import isPalindrome

line = sys.stdin.readline().strip()
arr = list(map(int, line.split())) if line else []
r = isPalindrome(arr)
print("true" if r else "false")
