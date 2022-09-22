# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        
        left, right = 0, 0
        count, product = 0, 1
        
        while len(nums) > right:
            product *= nums[right]
            
            while product >= k:
                product /= nums[left]
                left += 1
            
            count += right - left + 1
            right += 1
        
        return count

print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))