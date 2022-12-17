class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary(object):

    def __init__(self):
        self.head = TrieNode()
        self.max_word_length = 0

    def addWord(self, word):
        curr = self.head
        self.max_word_length = max(self.max_word_length, len(word))

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        
        curr.endOfWord = True
        
    def search(self, word):
        if len(word) > self.max_word_length:
            return False
        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child): return True
                    return False
                else:
                    if c not in curr.children: return False
                    curr = curr.children[c]
                
            return curr.endOfWord
        
        return dfs(0, self.head)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)