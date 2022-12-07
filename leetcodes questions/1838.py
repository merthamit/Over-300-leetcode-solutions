# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        l = total = maxLen = 0
        
        for r in range(len(nums)):
            total += nums[r]
            
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            
            maxLen = max(maxLen, (r - l + 1))
        
        return maxLen