class Solution(object):
    def islandPerimeter(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (r == ROWS or c == COLS or c < 0 or r < 0 or grid[r][c] != 1): return 1
            if (r, c) in visit: return 0
            
            visit.add((r, c))
            res = dfs(r, c+1)
            res += dfs(r, c-1)
            res += dfs(r+1, c)
            res += dfs(r-1, c)
            
            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r, c)
        

                        
        