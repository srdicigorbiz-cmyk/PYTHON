class Node:

    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def setValue(self, newVal):
        self.value = newVal

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def buildTreeInner(self, a):
        if a is None:
            return None
        node = Node()
        node.setValue(a[0])
        node.setLeft(self.buildTreeInner(a[1]))
        node.setRight(self.buildTreeInner(a[2]))
        return node

    def buildTree(self, s):
        a = eval(s.replace("null", "None"))
        self.root = self.buildTreeInner(a)

def getMaxPath(treeString):
    bt = BinaryTree()
    bt.buildTree(treeString)

    if bt.root is None:
        return 0
    
    def summing(node):
        if not node.getLeft() and not node.getRight():
            return node.getValue()
        elif node.getLeft() and node.getRight():
            return node.getValue() + max(summing(node.getLeft()), summing(node.getRight()))
        elif node.getLeft() and not node.getRight():
            return node.getValue() + summing(node.getLeft())
        elif not node.getLeft() and node.getRight():
            return node.getValue() + summing(node.getRight())
    
    return summing(bt.root)