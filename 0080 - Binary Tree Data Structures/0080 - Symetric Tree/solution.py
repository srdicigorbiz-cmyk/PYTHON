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

def isSymmetric(treeString):
    bt = BinaryTree()
    bt.buildTree(treeString)
    if bt.root is None:
        return True
    
    def isMirror(node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and node2:
            return (
            node1.getValue() == node2.getValue()
            and isMirror(node1.getLeft(), node2.getRight())
            and isMirror(node1.getRight(), node2.getLeft()) 
            )
        else:
            return False

    return isMirror(bt.root.getLeft(), bt.root.getRight())