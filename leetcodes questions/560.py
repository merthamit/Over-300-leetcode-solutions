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

# 15.09.2022 eğer çıkardığında sonuç soldaki topladığın sayılar kalan ise o zaman res += 1
# print(Solution().subarraySum([1,2,1,2,1], 3))
print(Solution().subarraySum([1,2,3,0,0,5,-2], 3))