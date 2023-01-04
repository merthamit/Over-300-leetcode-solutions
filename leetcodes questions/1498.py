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
                res += (2 ** (r - l)) # ---> subsequence bulurken (2 ** len(nums)) - 1 diye buluyoruz [1,2,3] --> 2 ** 3 - 1 = 8 subsequenci var
                res %= mod
            
            l += 1
                
        return res