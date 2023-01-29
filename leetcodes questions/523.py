class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder = { 0: -1 }
        
        currSum = 0
        for i, n in enumerate(nums):
            currSum += n
            remain = currSum % k
            
            if remain not in remainder:
                remainder[remain] = i
            elif i - remainder[remain] > 1:
                return True
                
        return False