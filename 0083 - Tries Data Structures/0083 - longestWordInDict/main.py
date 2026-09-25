import sys
from solution import longestWordInDict

line = sys.stdin.read().strip()
words = line.split() if line else []
print(longestWordInDict(words))
