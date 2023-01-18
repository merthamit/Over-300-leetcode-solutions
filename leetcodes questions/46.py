import collections
class Solution(object):
    def permute(self, nums):
        res = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
                
            res.extend(perms)
            nums.append(n)
            
        return res

class Solution(object):
    def permute(self, nums):
        perm, res = [], []
        count = collections.Counter(nums)
        
        def dfs():
            if len(nums) == len(perm):
                res.append(perm[:])
                return
            
            for n in count:
                if count[n]:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    
                    perm.pop()
                    count[n] += 1
        
        dfs()
        return res
    
        