class Solution2(object):
    def sortArrayByParity(self, nums):
        l = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums
        

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def sortArrayByParity(self, nums):
        l, r = 0, len(nums) - 1
        
        while r > l:
            if nums[l] % 2 > nums[r] % 2:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
            
            if nums[l] % 2 == 0: l += 1
            if nums[r] % 2 == 1: r -= 1
        
        return nums
    
print(Solution().sortArrayByParity([3,1,2,4]))