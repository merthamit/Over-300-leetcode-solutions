# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findLengthOfLCIS(self, nums):
        l, maxLen = 0, 0
        for r in range(len(nums)):
            if r > 0 and nums[r-1] >= nums[r]: l = r
            maxLen = max(maxLen, (r - l + 1))
        return maxLen 
            

print(Solution().findLengthOfLCIS([1,2,3,4,0,2,4,5,6,7]))
print(Solution().findLengthOfLCIS([2,2,2,2,2,2]))