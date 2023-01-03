import collections

class Solution(object):
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        times = fresh = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q and fresh:
            lng = len(q)
            
            for _ in range(lng):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    if (row == ROWS or col == COLS or col < 0 or row < 0 or grid[row][col] != 1): continue
                    
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
                    
            times += 1
    
        return times if fresh == 0 else -1
# Neden fresh kullanılıyor çünkü en sonda ki freshe gelindiği zaman yani 1'e tekrar çalışıyor ve hiçbir şekilde q'ya ekleyeceği bir direction olmadığı için