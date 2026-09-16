import sys
from solution import longestCommonPrefix

line = sys.stdin.read().strip()
words = line.split() if line else []
print(longestCommonPrefix(words))
