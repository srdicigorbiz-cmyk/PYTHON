import sys
from binarytree import BinaryTree

s = sys.stdin.readline().rstrip("\n")
bt = BinaryTree()
bt.buildTree(s)
bt.postOrderPrint()
