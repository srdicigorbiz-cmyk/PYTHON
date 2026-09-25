import sys
from solution import countWordsWithPrefix

lines = sys.stdin.read().split("\n")
words = lines[0].split() if lines and lines[0].strip() else []
prefix = lines[1] if len(lines) > 1 else ""
print(countWordsWithPrefix(words, prefix))
