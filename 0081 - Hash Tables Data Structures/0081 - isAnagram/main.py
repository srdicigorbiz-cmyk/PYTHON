import sys
from solution import isAnagram

data = sys.stdin.read().split('\n')
s1 = data[0]
s2 = data[1] if len(data) > 1 else ''
r = isAnagram(s1, s2)
print("true" if r else "false")
