class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children: return False
            curr = curr.children[c]
        
        return curr.endOfWord
                
    def startsWith(self, prefix):
        curr = self.root
        
        for c in prefix:
            if c not in curr.children: return False
            curr = curr.children[c]
        
        return True