class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        l, r = 0, k - 1
        res = float('inf')
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        
        return res