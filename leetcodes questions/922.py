# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def sortArrayByParityII(self, nums):
        l, r = 0, 1
        lng = len(nums)

        while lng > l and lng > r:
            while lng > l and nums[l] % 2 == 0:
                l += 2
            while lng > r and nums[r] % 2 == 1:
                r += 2
            
            if lng > l and lng > r:
                nums[l], nums[r] = nums[r], nums[l]

            l += 2
            r += 2
        
        return nums

print(Solution().sortArrayByParityII([3,1,4,2,5,6,7]))