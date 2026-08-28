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

    def setLeft(self, newLeft):
        self.left = newLeft

    def getRight(self):
        return self.right

    def setRight(self, newRight):
        self.right = newRight
