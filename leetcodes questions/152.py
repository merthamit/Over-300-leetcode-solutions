class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        currMax, currMin = 1, 1
        
        for n in nums:
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            print('currMax:', currMax, 'currMin:', currMin)
            res = max(res, currMax)
        
        return res
            
            
       