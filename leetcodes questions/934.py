import collections

class Solution(object):
    def shortestBridge(self, grid):
        N = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def invalid(r, c):
            return r == N or c == N or c < 0 or r < 0
        
        visit = set()
        def dfs(r, c):
            if invalid(r, c) or grid[r][c] != 1 or (r, c) in visit: return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(dr + r, dc + c)
                
        def bfs():
            res, q = 0, collections.deque(visit)
            
            while q:
                lng = len(q)
                
                for _ in range(lng):
                    row, col = q.popleft()

                    for dr, dc in directions:
                        r, c = dr + row, dc + col

                        if invalid(r, c) or (r, c) in visit: continue

                        if grid[r][c]: return res
                        
                        q.append((r, c))
                        visit.add((r, c))
                        
                res += 1
            
            return res
        
        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()