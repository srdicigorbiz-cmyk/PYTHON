from trie import Trie

def autocomplete(words, prefix):
    
    trie = Trie()

    if len(prefix) == 0:
        return sorted(words)

    for w in words:
        trie.insert(w)
    
    if not trie.startsWith(prefix):
        return []

    cur = trie.root
    
    result = []

    for p in prefix:
        cur = cur.children[p]

    

    def helper(node, prefix):

        if node.isEndOfWord:
            result.append(prefix)
    

        for ch in node.children:
            helper(node.children[ch], prefix + ch)
        
        
    
    helper(cur, prefix)
    return sorted(result)