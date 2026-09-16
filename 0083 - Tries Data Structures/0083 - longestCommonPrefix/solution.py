from trie import Trie

def longestCommonPrefix(words):
    
    trie = Trie()

    if len(words) == 0:
        return ""

    for w in words:
        trie.insert(w)
    
    cur = trie.root

    def helper(node):
        if len(node.children) == 1 and not node.isEndOfWord:
            c = list(node.children)[0]
            return str(c) + str(helper(node.children[c]))
        else:
            return ""
        
       
            
    return helper(cur)
    

    
    
