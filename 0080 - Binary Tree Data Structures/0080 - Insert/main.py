import sys
from binarytree import BinaryTree

bt = BinaryTree()
for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "insert":
        bt.insert(int(parts[1]))
    if cmd == "inOrderPrint":
        bt.inOrderPrint()
