# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# Prefixde ilk olarak solundaki sayıları bulup çarpıyor
# Postfixde ise sağındaki sayıların çarpımını buluyor ve bastırıyor.

print(Solution().productExceptSelf([1,2,3,4]))            