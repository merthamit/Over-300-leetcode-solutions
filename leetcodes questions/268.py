# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def missingNumber(self, nums):
        result = len(nums)

        for i in range(len(nums)):
            result += i - nums[i]
        
        return result

# Resulta len(nums) yazıyoruz çünkü i max len(nums) - 1 oluyor ondan.


print(Solution().missingNumber([0,2,3,4,5]))