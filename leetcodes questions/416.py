class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                nextDp.add(t)
                nextDp.add(t + nums[i])
            dp = nextDp
        
        return True if target in dp else False
        