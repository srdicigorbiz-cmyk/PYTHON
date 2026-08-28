import sys
from node import Node
from binarytree import BinaryTree

s = sys.stdin.readline().rstrip("\n")
bt = BinaryTree()
bt.buildTree(s)

def rtl(n):
    if n is None:
        return
    print(n.getValue())
    rtl(n.getRight())
    rtl(n.getLeft())

rtl(bt.getRoot())
