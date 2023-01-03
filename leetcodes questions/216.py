class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        N = 10
        
        def dfs(i, curr, total):
            if len(curr) == k and total == n:
                res.append(curr[:])
            
            if total > n or len(curr) == k: return
                
            for j in range(i, N):
                curr.append(j)
                dfs(j+1, curr, total + j)
                curr.pop()
        
        dfs(1, [], 0)
        return res
                
            