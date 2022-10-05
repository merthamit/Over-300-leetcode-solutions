# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r == ROWS or c == COLS or r < 0 or c < 0 or board[r][c] != 'O'): return
            board[r][c] = 'T'
            capture(r+1, c) 
            capture(r-1, c) 
            capture(r, c+1) 
            capture(r, c-1) 


        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1])):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        return board

        


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Yukarıdan su döküyormuşsun gibi düşün ve kapın bir yerini dolduruyor gibi.
print(Solution().solve(board))