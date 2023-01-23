class Solution(object):
    def letterCasePermutation(self, s):
        if not s: return []
        res = set()
        
        def dfs(i, curr):
            if len(s) == i:
                res.add(curr[:])
                return
            
            newS = curr[:i] + curr[i].upper() + curr[i+1:]
            dfs(i+1, newS) 
            newS = curr[:i] + curr[i].lower() + curr[i+1:]
            dfs(i+1, newS)
        
        dfs(0, s)
        return res

class Solution(object):
    def letterCasePermutation(self, s):
        if not s: return []
        res = set()
        
        def dfs(i, curr):
            if len(s) == i:
                res.add(curr[:])
                return
            
            newS = curr[:i] + curr[i].swapcase() + curr[i+1:]
            dfs(i+1, newS) 
            newS = curr
            dfs(i+1, newS)
        
        dfs(0, s)
        return res
            

class Solution(object):
    def letterCasePermutation(self, s):
        res = set()
        s = list(s)
        
        def dfs(i, curr):
            if len(s) == i:
                res.add(''.join(curr))
                return
            
            curr[i] = curr[i].upper()
            dfs(i+1, curr)
            curr[i] = curr[i].lower()
            dfs(i+1, curr)
            
        
        dfs(0, s)
        return res