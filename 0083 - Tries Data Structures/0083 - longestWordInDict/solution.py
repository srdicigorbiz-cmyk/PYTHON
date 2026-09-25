from trie import Trie

def longestWordInDict(words):

    trie = Trie()

    if not len(words):
        return ""

    for w in words:
        trie.insert(w)

    cur = trie.root
    path = ""
    result = []

    def helper(node, path):


        if node.isEndOfWord:
            result.append(path)
            

        for ch in node.children:
            if node.children[ch].isEndOfWord:
                helper(node.children[ch], path + ch)
            
            
    
    helper(cur, path)

    return max(sorted(result), key = len, default="")
            



    

