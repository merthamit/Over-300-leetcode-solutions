# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        currSum = 0
        prefixSum = { 0: 1 }

        for i in nums:
            currSum += i
            diff = currSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        
        return res


# print(Solution().subarraySum([1,2,1,2,1], 3))
print(Solution().subarraySum([1,2,3,0,0,5,-2], 3))
# print(Solution().subarraySum([3, 3 ,3], 3))
# print(Solution().subarraySum([-1,1,0], 0))
# print(Solution().subarraySum([1,1,1], 2))
# print(Solution().subarraySum([10, 20 , 30 , 40], 2))
