from trie import Trie

def countWordsWithPrefix(words, prefix):
    
    trie = Trie()

    if len(prefix) == 0:
        return len(words)

    for w in words:
        trie.insert(w)

    if not trie.startsWith(prefix):
        return 0

    cur = trie.root

    for p in prefix:
        if p in cur.children:
            cur = cur.children[p]
        else:
            return 0

    

    def helper(node):

        result = []

        if node.isEndOfWord and len(node.children) == 0:
            result.append(1)
        else:
            for ch in node.children:
                if node.isEndOfWord and len(node.children) > 0:
                    result.append(1+helper(node.children[ch]))
                else:
                    result.append(helper(node.children[ch]))
        
        return sum(result)
                
        
    
    return helper(cur)