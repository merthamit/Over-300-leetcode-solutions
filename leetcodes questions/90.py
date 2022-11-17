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