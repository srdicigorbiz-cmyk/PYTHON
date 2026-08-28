from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, newRoot):
        self.root = newRoot

    def _parse(self, s):
        s = s.strip()
        if s == 'null':
            return None
        # strip outer brackets
        inner = s[1:-1]
        # find first comma at depth 0 -> end of value
        depth = 0
        i = 0
        while i < len(inner):
            ch = inner[i]
            if ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
            elif ch == ',' and depth == 0:
                break
            i += 1
        value_str = inner[:i].strip()
        rest = inner[i+1:]
        # find next comma at depth 0 in rest -> split left and right
        depth = 0
        j = 0
        while j < len(rest):
            ch = rest[j]
            if ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
            elif ch == ',' and depth == 0:
                break
            j += 1
        left_str = rest[:j].strip()
        right_str = rest[j+1:].strip()
        node = Node()
        node.setValue(int(value_str))
        node.setLeft(self._parse(left_str))
        node.setRight(self._parse(right_str))
        return node

    def buildTree(self, treeString):
        self.root = self._parse(treeString)

    def _preOrder(self, node):
        if node is None:
            return
        print(node.getValue(), end=' ')
        self._preOrder(node.getLeft())
        self._preOrder(node.getRight())

    def preOrderPrint(self):
        self._preOrder(self.root)

    def _inOrder(self, node):
        if node is None:
            return
        self._inOrder(node.getLeft())
        print(node.getValue(), end=' ')
        self._inOrder(node.getRight())

    def inOrderPrint(self):
        self._inOrder(self.root)
