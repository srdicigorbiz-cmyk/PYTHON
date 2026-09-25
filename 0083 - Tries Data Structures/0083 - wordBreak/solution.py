from trie import Trie

def wordBreak(s, dictionary):
    
    trie = Trie()

    if len(s) == 0:
        return True

    for d in dictionary:
        trie.insert(d)

    cur = trie.root

    dp = [False] * (len(s)+1)
    
    dp[0] = True
    
    for i in range(len(s)):
        if dp[i]:
            cur = trie.root
            j = i
            while j < len(s):
                if s[j] in cur.children:
                    if cur.children[s[j]].isEndOfWord:
                        dp[j+1] = True        
                    cur = cur.children[s[j]]
                    j += 1
                else:
                    break    
                        
    return dp[len(s)]
    
    