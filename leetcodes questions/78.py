class Solution(object):
    def subsets(self, nums):
        if not nums: return nums
        res = []

        def backTrack(currArr, start):
            res.append(currArr)
            for n in range(start, len(nums)):
                backTrack(currArr + [nums[n]], n+1)
                
        backTrack([], 0)
        return res

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def subsets(self, nums):
        if not nums: return nums
        res = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res