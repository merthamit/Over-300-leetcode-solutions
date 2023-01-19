class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        res = []
        l, r = 0, len(nums) - 1
        
        while len(nums) != len(res):
            res.append(nums[l])
            l += 1
            
            if r >= l:
                res.append(nums[r])
                r -= 1
        
        return res