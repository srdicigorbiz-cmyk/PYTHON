import sys
from stack import Stack

stack = Stack()
for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "push":
        stack.push(int(parts[1]))
    elif cmd == "pop":
        print(stack.pop())
    elif cmd == "top":
        print(stack.top())
    elif cmd == "size":
        print(stack.size())
    elif cmd == "min":
        print(stack.min())
    elif cmd == "max":
        print(stack.max())
