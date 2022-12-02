# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def backTrack(r, c, i):
            if i == len(word): return True
            if (r == ROWS or c == COLS or c < 0 or r < 0 or word[i] != board[r][c] or (r, c) in path): return False
            
            
            path.add((r, c))
            res = (
            backTrack(r+1, c, i+1) or 
            backTrack(r-1, c, i+1) or 
            backTrack(r, c+1, i+1) or
            backTrack(r, c-1, i+1)
            )
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backTrack(r, c, 0): return True
                    
        return False

            
            
        