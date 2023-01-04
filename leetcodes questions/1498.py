class Solution(object):
    def numSubseq(self, nums, target):
        nums.sort()
        res = 0
        mod = (10 ** 9 + 7)
        
        l, r = 0, len(nums) - 1
        
        while len(nums) > l:
            while (nums[l] + nums[r]) > target and l <= r:
                r -= 1
            
            if l <= r:
                res += (2 ** (r - l))
                res %= mod
            
            l += 1
                
        return res