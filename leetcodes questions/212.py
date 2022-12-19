class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.refs = 0
        
    def addWord(self, word):
        curr = self
        curr.refs += 1

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1

        curr.endOfWord = True
        curr.fullyWord = word
                
    
    def removeWord(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1


class Solution(object):
    def findWords(self, board, words):
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        
        for word in words:
            root.addWord(word)
        
        res, visit = [], set()
        
        def dfs(r, c, node):
            if (r == ROWS or c == COLS or c < 0 or r < 0 or (r, c) in visit or board[r][c] not in node.children or node.children[board[r][c]].refs < 1): return False
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            if node.endOfWord: 
                node.endOfWord = False
                res.append(node.fullyWord)
                root.removeWord(node.fullyWord)
                
            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c-1, node)
            dfs(r, c+1, node)
            
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return res
        
        
        