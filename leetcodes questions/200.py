import collections


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def numIslands(self, grid):
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(len(grid)) and c in range(len(grid[0])) and (r, c) not in visit and grid[r][c] == '1'):
                        q.append((r, c))
                        visit.add((r, c))
                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    bfs(r, c)
        
        return islands



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(grid))