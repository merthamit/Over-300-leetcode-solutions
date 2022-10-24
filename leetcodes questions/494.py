class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {}
        
        def backTrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backTrack(i+1, total+nums[i]) + backTrack(i+1, total-nums[i]))
            
            return dp[(i, total)]
            
        return backTrack(0, 0)