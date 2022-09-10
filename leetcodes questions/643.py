# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findMaxAverage(self, nums, k):
        start = 0
        maxSum = currSum = sum(nums[:k])

        for end in range(k, len(nums)):
            currSum += nums[end]

            if (end - start + 1) >= k:
                currSum -= nums[start]
                maxSum = max(maxSum, currSum)
                start += 1
        
        return float(maxSum) / k

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))