# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0

            curSum += i
            maxSub = max(maxSub, curSum)
        
        return maxSub


# Sayıyı arttır save al ilerde array büyüdükçe karşılaştırma yap.
print(Solution().maxSubArray([-2,6,-3,-4,2,4,1]))