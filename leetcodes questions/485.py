class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxLen = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                maxLen = max(maxLen, (r - l + 1))
            else:
                l = r + 1
                
            
        return maxLen
    
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))