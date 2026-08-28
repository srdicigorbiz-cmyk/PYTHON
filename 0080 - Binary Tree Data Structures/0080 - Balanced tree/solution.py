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

def getHeight(node):
    if node is None:
        return 0
    else:
        return 1 + max(getHeight(node.getLeft()) , getHeight(node.getRight()))


def isBalanced(treeString):
    bt = BinaryTree()
    bt.buildTree(treeString)
    root = bt.getRoot()


    def balance_sides(root):
        
        if root is None:
            return True

        if abs(getHeight(root.getLeft()) - getHeight(root.getRight())) <= 1:
            return True
        else:
            return False


    return balance_sides(root)