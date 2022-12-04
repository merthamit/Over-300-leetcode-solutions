# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        
        
        def backTrack(i, subSet):
            if i == len(nums):
                res.append(subSet[:])
                return
            
            subSet.append(nums[i])
            backTrack(i+1, subSet)
            subSet.pop()
            
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
                
            backTrack(i+1, subSet)
            
            
            
        backTrack(0, [])
        return res

class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        
        def backTrack(i, curr):
            res.append(curr[:])
            
            prev = None
            for j in range(i, len(nums)):
                if prev == nums[j]: continue
                curr.append(nums[j])
                backTrack(j+1, curr)
                prev = nums[j]
                curr.pop()
            
        backTrack(0, [])
        return res