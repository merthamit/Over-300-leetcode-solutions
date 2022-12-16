class Solution(object):
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        for i in range(len(nums)-3, -1, -1):
            currMax = nums[i+2]
            for j in range(i+2, len(nums)):
                currMax = max(currMax, nums[j])
            nums[i] += currMax
        
        return max(nums[0], nums[1])

class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
                