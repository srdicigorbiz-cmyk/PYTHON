from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, newRoot):
        self.root = newRoot

    def parse(self, data):
        if data is None:
            return None

        node = Node()
        node.setValue(data[0])

        node.setLeft(self.parse(data[1]))

        node.setRight(self.parse(data[2]))

        return node

    def buildTree(self, s):
        data = eval(s.replace("null", "None"))
        self.root = self.parse(data)