class Solution(object):
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(r, c, visit, prevHeight):
            if (r == ROWS or c == COLS or r < 0 or c < 0 or prevHeight > heights[r][c] or (r, c) in visit): return
            
            visit.add((r, c))
            
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res


