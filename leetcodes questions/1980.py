class Solution(object):
    def findDifferentBinaryString(self, nums):
        visit = set(nums)
        res = ['']
        
        def dfs(curr):
            if len(nums) == len(curr) and ''.join(curr) not in visit:
                res[0] = ''.join(curr)
                return
            
            if len(nums) <= len(curr) or res[0]: return
            
            curr.append('1')
            dfs(curr)
            curr.pop()
            curr.append('0')
            dfs(curr)
            curr.pop()
        
        dfs([])
        return res[0]

class Solution(object):
    def findDifferentBinaryString(self, nums):
        strSet = { s for s in nums }
        
        def backTrack(i, curr):
            if len(nums) == i:
                res = ''.join(curr)
                return None if res in strSet else res
            
            res = backTrack(i+1, curr)
            if res: return res
            
            curr[i] = '1'
            res = backTrack(i+1, curr)
            if res: return res
            
        return backTrack(0, ['0' for s in nums])
            
        
                
            
        