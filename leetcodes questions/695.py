# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxAreaOfIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or c == COLS or r == ROWS or grid[r][c] != 1 or (r, c) in visit): return 0
            visit.add((r, c))
            return (1 + 
            dfs(r, c+1) +
            dfs(r, c-1) +
            dfs(r+1, c) +
            dfs(r-1, c)
            )

        maxCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxCount = max(maxCount, dfs(r, c))
        
        return maxCount
                    
                    
            
        
