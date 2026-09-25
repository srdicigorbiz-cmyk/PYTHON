from trienode import TrieNode


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEndOfWord

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    def delete(self, word):
        def helper(node, depth):
            if depth == len(word):
                node.isEndOfWord = False
                return len(node.children) == 0
            c = word[depth]
            if c not in node.children:
                return False
            should_remove_child = helper(node.children[c], depth + 1)
            if should_remove_child:
                del node.children[c]
                return (not node.isEndOfWord) and (len(node.children) == 0)
            return False
        helper(self.root, 0)

    def wordCount(self):
        def helper(node):
            cnt = 1 if node.isEndOfWord else 0
            for ch in node.children.values():
                cnt += helper(ch)
            return cnt
        return helper(self.root)
