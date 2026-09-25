import sys
from solution import wordBreak

lines = sys.stdin.read().split("\n")
s = lines[0] if len(lines) > 0 else ""
d_line = lines[1] if len(lines) > 1 else ""
dictionary = d_line.split() if d_line.strip() else []



print("true" if wordBreak(s, dictionary) else "false")
